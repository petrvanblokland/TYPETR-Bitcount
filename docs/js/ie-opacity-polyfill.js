/**
 * Internet Explorer opacity polyfill by http://blade.sk
 *
 * Licensed under MIT
 * http://www.opensource.org/licenses/mit-license.php
 *
 * Version : 1.1
 */
(function() {

	// IE 6-8 only
	if (!navigator.userAgent.match(/msie [6-8]/i)) return;

	// wait until the DOM is ready
	var _domReadyTimer = setInterval(function() {
		if (/loaded|complete/.test(document.readyState)) {

			clearInterval(_domReadyTimer);

			// go through all the CSS rules and add the alpha filter
			for (var si = 0; si < document.styleSheets.length; si++) {
				try
				{
					for (var ri = 0; ri < document.styleSheets[si].rules.length; ri++) {
						if (typeof document.styleSheets[si].rules[ri].style.opacity != 'undefined') {
							var val = document.styleSheets[si].rules[ri].style.opacity;
							document.styleSheets[si].rules[ri].style.filter = 'alpha(opacity='+Math.round(val*100)+')';
						}
					}
				}
				catch (e) {} // IE 6-7 doesn't allow accessing cross-site stylesheets
			}
			////
		}
	}, 10);

})();