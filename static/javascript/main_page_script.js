document.addEventListener('DOMContentLoaded', function() {
      const countries = document.querySelectorAll('.country');
      countries.forEach(country => {
        country.addEventListener('click', function() {
          const content = this.querySelector('.content');
          countries.forEach(otherCountry => {
            if (otherCountry !== this) {
              otherCountry.querySelector('.content').style.display = 'none';
            }
          });
          if (content.style.display === 'none') {
            content.style.display = 'block';
          } else {
            content.style.display = 'none';
          }
        });
      });
    });

document.addEventListener('DOMContentLoaded', function() {
      const countries = document.querySelectorAll('.scenario');
      countries.forEach(country => {
        country.addEventListener('click', function() {
          const content = this.querySelector('.content');
          countries.forEach(otherCountry => {
            if (otherCountry !== this) {
              otherCountry.querySelector('.content').style.display = 'none';
            }
          });
          if (content.style.display === 'none') {
            content.style.display = 'block';
          } else {
            content.style.display = 'none';
          }
        });
      });
    });