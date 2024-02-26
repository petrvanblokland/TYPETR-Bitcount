    // Check if the browser is Chrome
    var isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);

    // Function to update the sample text style
    function updateTextStyle() {
      const weight = document.getElementById('weight-slider').value;
      const elementOpen = document.getElementById('ELXP-slider').value;
      const elementShape = document.getElementById('ELSH-slider').value;
      const slant = document.getElementById('slant-slider').value;
      const size = document.getElementById('size-slider').value;
      // COLRv1 
      const bgSize = document.getElementById('bgSize-slider').value;
      const bgX = document.getElementById('bgX-slider').value;
      const bgY = document.getElementById('bgY-slider').value;
      const fgSize = document.getElementById('fgSize-slider').value;
      const fgX = document.getElementById('fgX-slider').value;
      const fgY = document.getElementById('fgY-slider').value;

      const sampleText1 = document.getElementById('color-sample-text1');
      sampleText1.style.fontVariationSettings = `'wght' ${weight}, 'ELXP' ${elementOpen}, 'ELSH' ${elementShape}, 'slnt' ${slant},
        'SZP1' ${bgSize}, 'XPN1' ${bgX}, 'YPN1' ${bgY}, 
        'SZP2' ${fgSize}, 'XPN2' ${fgX}, 'YPN2' ${fgY}`;
      sampleText1.style.fontSize = `${size}px`;

      const sampleText2 = document.getElementById('color-sample-text2');
      sampleText2.style.fontVariationSettings = `'wght' ${weight}, 'ELXP' ${elementOpen}, 'ELSH' ${elementShape}, 'slnt' ${slant},
        'SZP1' ${bgSize}, 'XPN1' ${bgX}, 'YPN1' ${bgY}, 
        'SZP2' ${fgSize}, 'XPN2' ${fgX}, 'YPN2' ${fgY}`;
      sampleText2.style.fontSize = `${size}px`;
    }

  // Event listeners for sliders
  const sliders = document.querySelectorAll('.slider');
  sliders.forEach(slider => {
    slider.addEventListener('input', updateTextStyle);
  });

  // Initial call to set the sample text style
  updateTextStyle();

    if (isChrome) {
      document.write("<p>This page is running on Chrome browser.</p>");
    } else {
      document.write("<p>This page is not running on Chrome browser.</p>");
    }

  // Get the sample text element
  const sampleText1 = document.getElementById('sample-text1');
  const sampleText2 = document.getElementById('sample-text2');

  angleELSH = 0; // Shaping the pixel
  angleELXP = 0; // Open pixel in quadrants

  angleSZP1 = 0;
  angleXPN1 = 0;
  angleYPN1 = 0;
  angleSZP2 = 0;
  angleXPN2 = 0;
  angleYPN2 = 0;

  const stepELSH = 6; // Increment of the cycle angles
  const stepELXP = 5;
  const stepSZP1 = 3;
  const stepXPN1 = 5;
  const stepYPN1 = 7;
  const stepSZP2 = 4;
  const stepXPN2 = 6;
  const stepYPN2 = 8;

  stepFactor = 0.5 // Overall speed factor for steps

  const minELSH = 700;
  const minELXP = 0;
  const minSZP1 = 0;
  const minXPN1 = -50;
  const minYPN1 = -50;
  const minSZP2 = 50;
  const minXPN2 = -100;
  const minYPN2 = -100;

  const maxELSH = 1000;
  const maxELXP = 800; // Not too open in this animation
  const maxSZP1 = 1000;
  const maxXPN1 = 50;
  const maxYPN1 = 50;
  const maxSZP2 = 500;
  const maxXPN2 = 100;
  const maxYPN2 = 100;

  function normalizeAngle(angle) {
      return (angle % 360 + 360) % 360;
  }

  function updateValues() {
    valELSH = (Math.sin((angleELSH * Math.PI/180))/2 + 0.5) * (maxELSH - minELSH) + minELSH;
    document.getElementById('ELSH-slider').value = valELSH;

    valELXP = (Math.sin((angleELXP * Math.PI/180))/2 + 0.5) * (maxELXP - minELXP) + minELXP;
    document.getElementById('ELXP-slider').value = valELXP;

    valSZP1 = (Math.sin((angleSZP1 * Math.PI/180))/2 + 0.5) * (maxSZP1 - minSZP1) + minSZP1;
    document.getElementById('bgSize-slider').value = valSZP1;

    valXPN1 = (Math.sin((angleXPN1 * Math.PI/180))/2 + 0.5) * (maxXPN1 - minXPN1) + minXPN1;
    document.getElementById('bgX-slider').value = valXPN1;

    valYPN1 = (Math.sin((angleYPN1 * Math.PI/180))/2 + 0.5) * (maxYPN1 - minYPN1) + minYPN1;
    document.getElementById('bgY-slider').value = valYPN1;

    valSZP2 = (Math.sin((angleSZP2 * Math.PI/180))/2 + 0.5) * (maxSZP2 - minSZP2) + minSZP2;
    document.getElementById('fgSize-slider').value = valSZP2;

    valXPN2 = (Math.sin((angleXPN2 * Math.PI/180))/2 + 0.5) * (maxXPN2 - minXPN2) + minXPN2;
    document.getElementById('fgX-slider').value = valXPN2;

  }
  // Function to animate through all axes smoothly
  function animateVariableFont() {
    updateValues();

    angleELSH = normalizeAngle(angleELSH + stepELSH * stepFactor);
    angleELXP = normalizeAngle(angleELXP + stepELXP * stepFactor);
    angleSZP1 = normalizeAngle(angleSZP1 + stepSZP1 * stepFactor);
    angleXPN1 = normalizeAngle(angleXPN1 + stepXPN1 * stepFactor);
    angleYPN1 = normalizeAngle(angleYPN1 + stepYPN1 * stepFactor);
    angleSZP2 = normalizeAngle(angleSZP2 + stepSZP2 * stepFactor);
    angleXPN2 = normalizeAngle(angleXPN2 + stepXPN2 * stepFactor);
    angleYPN2 = normalizeAngle(angleYPN2 + stepYPN2 * stepFactor);

    updateTextStyle();
    //sampleText1.style.fontVariationSettings = "'SZP1' ${valSZP1}, 'XPN1' ${valXPN1}, 'XPN1' ${valXPN1}, 'SZP2' ${valSZP2}, 'XPN2' ${valXPN2}, 'XPN2' ${valXPN2}, ";

  }
