const darkModeToggle = document.getElementById('darkmodebtn');
var section = document.getElementById('bgkc');
var header = document.getElementById('hedr');
var card = document.getElementById('cards');

const savedMode = localStorage.getItem('darkMode');
if (savedMode === 'dark') {
  enableDarkMode();
}

function enableDarkMode() {
  if(section){
    section.classList.add('dark-mode');
  }
  header.classList.add('dark-mode');
  if(card){
    card.classList.add('dark-mode');
  }
  localStorage.setItem('darkMode', 'dark');
}

function disableDarkMode() {
  if(section){
    section.classList.remove('dark-mode');
  }
  header.classList.remove('dark-mode');
  if(card){
    card.classList.remove('dark-mode');
  }
  localStorage.setItem('darkMode', 'light');
}

darkModeToggle.addEventListener('click', () => {
  const isDarkModeEnabled = header.classList.contains('dark-mode');

  if (isDarkModeEnabled) {
    disableDarkMode();
  } else {
    enableDarkMode();
  }
});
