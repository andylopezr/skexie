const $ = window.$;
const fetch = window.fetch;

// Fetch POST function definition.
async function skexieCall (input = '') {
  const url = 'http://localhost:5000/api';
  // const url = 'http://ec2-54-187-163-241.us-west-2.compute.amazonaws.com/api';
  const data = { text: input };
  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return response.text();
}

document.onreadystatechange = function () {
  if (document.readyState === 'complete') {

    // Toggle side menubar. - - - - - - - - - - - - - - - - - - - - - - - - - |
    $('.burger').click(function () {
      $('.bar-menu').css('display', 'block');
      $('.mobile-exit').css('display', 'block');
    });
    $('.mobile-exit').click(function () {
      $('.bar-menu').css('display', 'none');
    });
    $('.bar-menu a').click(function () {
      $('.bar-menu').css('display', 'none');
    });

    // Check if input box has text on it on keyup action.- - - - - - - - - -|
    $('.input-box').keyup(function () {
      const text = $('.input-box').val();
      if (text) {
        $('.submit').css('color', '#4aa96c');
        $('.submit').css('border-color', '#4aa96c');
      } else {
	if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
          $('.submit').css('color', '#FFFFFF');
          $('.submit').css('border-color', '#FFFFFF');
	} else {
          $('.submit').css('color', '#564a4a');
          $('.submit').css('border-color', '#564a4a');
	}
      }
    });

    // Check if submit button was clicked.- - - - - - - - - - - - - - - - - - |
    $('.submit').click(async function () {
      const text = $('.input-box').val();
      if (text) {
	$('.submit').off('click');
	$('.text-placeholder').css('display', 'none');
        if (window.matchMedia('(orientation: portrait)').matches) {
          $('.input-box').css('display', 'none');
        }
        $('.try-area h1').text('Processing...');
        $('.submit').text('Please Wait...');

        skexieCall(text)
          .then(data => {
            const list = JSON.parse(data);
            $('.try-area h1').text('Got ' + list.length + ' skills.');
            list.forEach(function (item) {
              const skill = item.skill;
              const exp = item.experience;
              const li = document.createElement('li');
              const spanSkill = document.createElement('span');
              $(spanSkill).addClass('skill');
              spanSkill.appendChild(document.createTextNode(skill));
              const spanExp = document.createElement('span');
              $(spanExp).addClass('experience');
              spanExp.appendChild(document.createTextNode(exp));

              if (exp !== 0) {
                li.appendChild(spanExp);
                li.appendChild(document.createTextNode(' years in '));
                li.appendChild(spanSkill);
              } else {
                li.appendChild(document.createTextNode('Knowledge in '));
                li.appendChild(spanSkill);
              }
              $('.skill-list').append(li);
            });
            $('.try-area h1').css('color', '#4aa96c');
            $('.submit').text('Done');
            $('.submit').css('color', '#4aa96c');
            $('.submit').css('border-color', '#4aa96c');
            $('.skill-list').css('display', 'flex');
          });

      }
    });
  }
};
