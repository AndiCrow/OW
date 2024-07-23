
document.addEventListener('DOMContentLoaded', function() {
  var dropdowns = document.querySelectorAll('.dropdown > a');
  dropdowns.forEach(function(dropdown) {
      dropdown.addEventListener('click', function(event) {
          event.preventDefault();
          var menu = this.nextElementSibling;
          menu.classList.toggle('hidden');
      });
  });
})

for (let i = 0; i < dropdowns.length; i++) {
  dropdowns[i].addEventListener("click", toggleDropdown);
}



  