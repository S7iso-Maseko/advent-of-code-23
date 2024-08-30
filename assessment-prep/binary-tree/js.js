let transcript = '';

const SpeechRecognition = window.speechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.lang = 'en-US';

// recognition.continuous = true;

const parent = document.getElementsByClassName('relative flex h-full flex-1 md:flex-col');
const regen = document.getElementsByClassName('flex ml-1 mt-1.5 md:w-full md:m-auto md:mb-2 gap-0 md:gap-2 justify-center')[0].style.border = '1px solid gray';
document.getElementsByClassName('flex ml-1 mt-1.5 md:w-full md:m-auto md:mb-2 gap-0 md:gap-2 justify-center')[0].style.borderRadius = '8px';


const button = document.createElement('button');
const button2 = document.createElement('button');
const img = document.createElement('img');


img.src = 'https://cdn3.iconfinder.com/data/icons/social-messaging-ui-line-shapes-1/3/06-512.png';

img.style.width = '45px';
img.style.margin = '9px';
// regen.style.borderRadius = '8px';

button.innerHTML = '';
button.appendChild(img);

button2.innerText = 'Stop';
parent[0].appendChild(button);

button.classList.add('my-class');

const style = document.createElement('style');
style.textContent = `
  .my-class {
    position: absolute;
    right: -9%;
    top: 8%;
    max-height: 63px;
  }


  button img {
    transition: all 0.5s ease;
  }

  button img:hover {
    transform: scale(1.1);
    margin: 12px;
  }
`;

// Append the style element to the head of the document
document.head.appendChild(style);

button.addEventListener('click', () => {
    recognition.start();
    img.src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Circle-icons-mic.svg/512px-Circle-icons-mic.svg.png';
});


recognition.addEventListener("result", (event) => {
    transcript = Array.from(event.results)
                .map(result => result[0])
                .map(result => result.transcript)
                .join('');

    img.src = 'https://cdn3.iconfinder.com/data/icons/social-messaging-ui-line-shapes-1/3/06-512.png';

});

recognition.addEventListener("end", () => {
    recognition.stop();
    img.src = 'https://cdn3.iconfinder.com/data/icons/social-messaging-ui-line-shapes-1/3/06-512.png';

    document.getElementsByClassName('m-0 w-full resize-none border-0 bg-transparent p-0 pl-2 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent md:pl-0')[0].value = transcript;

    document.getElementsByClassName('absolute p-1 rounded-md text-gray-500 bottom-1.5 right-1 md:bottom-2.5 md:right-2 hover:bg-gray-100 dark:hover:text-gray-400 dark:hover:bg-gray-900 disabled:hover:bg-transparent dark:disabled:hover:bg-transparent')[0].click();
    document.getElementsByClassName('flex ml-1 mt-1.5 md:w-full md:m-auto md:mb-2 gap-0 md:gap-2 justify-center')[0].style.borderRadius = '8px';
    transcript = '';
});


recognition.addEventListener("error", (event) => {
    console.error("Error occured in recognition ", event.error);
    img.src = 'https://cdn3.iconfinder.com/data/icons/social-messaging-ui-line-shapes-1/3/06-512.png';
});