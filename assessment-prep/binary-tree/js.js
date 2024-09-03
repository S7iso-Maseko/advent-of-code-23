let fs = require('fs');
let axios = require('axios');
let path = require('path');
let mkdirp = require('mkdirp');
let moment = require('moment');
let XMLHttpRequest = require('xhr2');
const { browser } = require('protractor');
let screenShotTimeStamp = moment();

describe('BOP Form Regression Testing', function () {

    let currentTestName = '';
    let errorTestName = '';

    // browser.driver.manage().window().maximize();

    // // // TO PREVENT JASMINE FROM TIMING OUT // // // 
    beforeEach(() => {
        browser.driver.manage().window().setSize(1920, 1080);
        originalTimeout = jasmine.DEFAULT_TIMEOUT_INTERVAL;
        jasmine.DEFAULT_TIMEOUT_INTERVAL = 1000000;
    });

    afterEach(() => {
        jasmine.DEFAULT_TIMEOUT_INTERVAL = originalTimeout;
    });
    // // // TO PREVENT JASMINE FROM TIMING OUT // // // 

    // // // FUNCTION CALLED WHEN YOU WANT TO TAKE A SCREENSHOT // // //
    function grabScreenshot(screenshotName) {
        browser.takeScreenshot().then((png) => {
            console.log("Screenshot taken.");
            writeScreenshot(png, screenshotName ? screenshotName : currentTestName);
        });
    } // // // END // // //

    //  // // SEND POST REQUESTS TO SWAGGER APIs, LOGIN AND LOAD DATA WITH REPORT API // // //
    async function sendRequest(filepath, loadAPI) {
        fs.readFile(filepath, async (err, data) => {
            if (err) throw err;

            let xhr = new XMLHttpRequest();
            xhr.open("POST", loadAPI);
            xhr.setRequestHeader("Accept", "application/json");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.responseType = 'json';

            await xhr.send(data);

        });
    } //  // // END // // //


    async function sendXMLRequest(filepath, loadAPI) {
        fs.readFile(filepath, (err, data) => {
            if (err) throw err;

            let xhr = new XMLHttpRequest();
            xhr.open("POST", loadAPI);
            xhr.setRequestHeader("Content-Type", "application/xml");
            xhr.responseType = 'text';

            xhr.send(data);
        });
    } //  // // END // // //

    //  // // LOOP THROUGH DATA TO LOAD FROM DIFFERENT SCENARIOS // // //
    // (async function() {
    //     try {
    //       const data = await getData('https://jsonplaceholder.typicode.com/todos/1');
    //       console.log(JSON.parse(data));
    //     } catch (error) {
    //       console.error(error);
    //     }
    //   })();

    const scenarios = fs.readFileSync('./test-data/scenarios.json', 'UTF-8');
    const testPaths = JSON.parse(scenarios.toString());
    Object.keys(testPaths).forEach((paths) => {
        testPaths[paths].forEach((path) => {
            (async function () {
                try {
                    await sendRequest(path.testDataPath, path.loadAPI);

                    if (path.accountEntry === true) {
                        await sendXMLRequest(path.accountEntryPath, path.acAPI);
                        setTimeout(async () => {
                            await sendRequest(path.statePath, path.state);
                        }, 3000);
                    }
                } catch (error) {
                    console.error(error);
                }
            })();
        });
    }); //  // // END // // //

    // LONG SLEEP
    // browser.sleep(15000);

    // // // TO LOOP THROUGH ALL THE TEST CASES AND PERFORM THE ACTIONS // // //
    const content = fs.readFileSync('./test-data/test-packs.json', 'UTF-8');
    const testPacks = JSON.parse(content.toString());

    testPacks.channelPacks.forEach((channelpack) => {
        const testpackContent = fs.readFileSync(channelpack.TestPacks, 'UTF-8');
        const testpackFile = JSON.parse(testpackContent.toString());

        Object.keys(testpackFile).forEach((testpackName) => {

            testpackFile[testpackName].forEach((testpack) => {

                const testcaseContent = fs.readFileSync(testpack.Scenario, 'UTF-8');
                const testcaseFile = JSON.parse(testcaseContent.toString());

                it('Test-Cases', () => {
                    if (typeof Object.keys(testcaseFile) !== 'undefined') {
                        browser.get(testpack.url).then(() => {
                            browser.sleep(1000);
                            let testNumber = 0;
                            Object.keys(testcaseFile).forEach((testcase) => {
                                testcaseFile[testcase].forEach((task) => {
                                    let testNumberStr = "00000" + testNumber;
                                    testNumberStr = testNumberStr.substr(testNumberStr.length - 5);
                                    if (task.action == "link") {
                                        element(by.xpath(task.alink)).click();
                                        browser.sleep(task.sleep);
                                    } else if (task.action == "link2") {
                                        element(by.xpath(task.alink)).click().click();
                                        browser.sleep(task.sleep);
                                    } else if (task.action == "input") {
                                        element(by.xpath(task.input_link)).clear();
                                        element(by.xpath(task.input_link)).click().sendKeys(task.input);
                                    } else if (task.action == "dropdown") {
                                        element(by.xpath(task.dropdown_link)).click().sendKeys(task.input);
                                        element(by.xpath(task.country_section)).click();
                                    } else if (task.action == "option") {
                                        element(by.xpath(task.select)).click();
                                        element(by.xpath(task.input)).click();
                                    }
                                    browser.sleep(200);
                                    currentTestName = testpack.channel + '-' + testcase + '-' + testNumberStr;
                                    errorTestName = testpack.channel + '-' + testcase + '-errors-' + testNumberStr;
                                });
                                testNumber++;
                                browser.sleep(400);
                                grabScreenshot(currentTestName);

                                element(by.xpath("/html/body/div/div/bopform/div[2]/error-list/div/a")).click();
                                browser.sleep(400);
                                grabScreenshot(errorTestName);
                                element(by.xpath("/html/body/div[1]/div/div/div[3]/div/a")).click();
                            });
                        });
                    }
                });
            });
        });
    });
});
 
async function getWindowData(filename) {
    var data = await browser.executeScript('return JSON.stringify(window.BOPForm.getData());');
    fs.appendFile(filename, data, function (err) {
        if (err) throw err;
    });
}

async function getWindowErrors(filename) {
    var data = await browser.executeScript('return JSON.stringify(window.BOPForm.getRaisedEvents());');
    fs.appendFile(filename, data, function (err) {
        if (err) throw err;
    });
}


function writeScreenshot(data, filename) {

    //Define the current timestamp which specifies the time at which a screenshot has been captured for a test

    let testTimestamp = screenShotTimeStamp.format('YYYY-MM-DD-HH-mm-ss');
    let dateTime = screenShotTimeStamp.format('YYYY-MM-DDTHH:mm:ss');
    let channel = filename.split('-');
    let screenShotFolder = "./screenshots/login-spec/" + "/" + channel[0] + "/" + testTimestamp;

    let data_dump = screenShotFolder + "/" + filename + ".data_dump.json";
    let raiseEvents = screenShotFolder + "/" + filename + ".raised_events.json";

    channel[2] != 'errors' ? (getWindowData(data_dump), getWindowErrors(raiseEvents)) : "";

    // There should be one output folder with one time stamp for all the screenshots
    let testDetails = {

        description: filename,
        spec: filename,
        file: filename + '.png',
        testResult: true,
        timestamp: testTimestamp,
        dateTime: dateTime
    };
    // Create the file paths for the screen shot and the json file that stores the details of the screenshot:
    let screenShotfilePath = path.join(screenShotFolder, filename + '.png');

    let jsonfilePath = path.join(screenShotFolder, filename + '.info.json');

    console.log('Screenshot File output path:' + screenShotfilePath);
    console.log('Screenshot Json File output path:' + jsonfilePath);

    // Make sure that the directory has been created:
    // NOTE: mkdirp is asynchronous, so we have to wait for the callback before we can write the screenshot to file.
    return mkdirp(screenShotFolder, function (error) {
        if (error) {
            console.log(error);
        } else {
            console.log('Directory created.');

            // Create the write stream:
            // NOTE: the write stream can only be created AFTER the directories exist.
            let screenshotStream = fs.createWriteStream(screenShotfilePath);

            let screenshotDetailsStream = fs.createWriteStream(jsonfilePath);
            //convert testDetails object to a string
            let testDetailsJson = JSON.stringify(testDetails);
            // Now that we have the directory, write the screenshot to a file:
            screenshotStream.write(new Buffer(data, 'base64'));

            console.log('Screenshot saved.');

            //Write the generated json to a file
            screenshotDetailsStream.write(testDetailsJson);

            console.log('Screenshot details saved');

            // No more data will be written:
            screenshotDetailsStream.end();
            screenshotStream.end();

        }
    });

}



var levenshtein = (function () {
    var row2 = [];
    return function (s1, s2) {
        if (s1 === s2) {
            return 0;
        } else {
            var s1_len = s1.length, s2_len = s2.length;
            if (s1_len && s2_len) {
                var i1 = 0, i2 = 0, a, b, c, c2, row = row2;
                while (i1 < s1_len)
                    row[i1] = ++i1;
                while (i2 < s2_len) {
                    c2 = s2.charCodeAt(i2);
                    a = i2;
                    ++i2;
                    b = i2;
                    for (i1 = 0; i1 < s1_len; ++i1) {
                        c = a + (s1.charCodeAt(i1) === c2 ? 0 : 1);
                        a = row[i1];
                        b = b < a ? (b < c ? b + 1 : c) : (a < c ? a + 1 : c);
                        row[i1] = b;
                    }
                }
                return b;
            } else {
                return s1_len + s2_len;
            }
        }
    };
})();

// const s1Content = fs.readFileSync("./screenshots/login-spec/sbZA/2022-11-29-17-17-37/sbZA-TestCase001-00001.data_dump.json", 'UTF-8');
// const s1 = s1Content.toString();

// const s2Content = fs.readFileSync("./screenshots/login-spec/sbZA/2022-11-29-16-48-18/sbZA-TestCase001-00000.data_dump.json", 'UTF-8');
// const s2 = s2Content.toString();

// let distance = levenshtein(s1, s2);
// console.log("\n\n\n LEVEN LEVENLEVENLEVENLEVENLEVENLEVENLEVENLEVENLEVENLEVEN", distance, "\n\n\n");


//    element(by.id('PaymentDetail.SWIFTDetails').sendKeys("dummy data");
//    browser.driver.sleep(10000)
//   browser.element(by.id("PaymentDetail.SWIFTDetails"))

////////////////////////////////////////////////////////////
//Step 2) Enter values in the input fields
//////////////////////////////////////



// FOR WHEN YOU WANT TO TAKE SCREENSHOTS AFTER EVERY ITERATION OF THE IT BLOCK

//    afterEach(async function () {
//        console.log('After Each:');
//        // Take a screenshot as soon as the test has completed:
//        await browser.takeScreenshot().then((png) => {
//            console.log("Screenshot taken.");
//            writeScreenshot(png, currentTestName);
//        });
//    });


// FOR WHEN I WANT TO TAKE SCREENSHOTS OF ERROR-DROPDOWN

// element(by.xpath("/html/body/div/div/bopform/div[2]/error-list/div/a")).click();
// currentTestName = "Errors" + '-' + testNumber;
// grabScreenshot(currentTestName);
// element(by.xpath("/html/body/div[1]/div/div/div[3]/div/a")).click();