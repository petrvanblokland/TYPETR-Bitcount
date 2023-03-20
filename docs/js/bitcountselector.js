

var layerCnt = 4;
var posture = 'italic'; /* Will toggle on init to roman. */
var border = '1px solid #0000FF';
var doShift = true;
var doOpacity = true;
/* Pixels type selection */
var doSingle = true;
var doDouble = true;
var doCircle = true;
var doOpenCircle = true;
var doSquare = true;
var doOpenSquare = true;
var doPlus = true;

function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}
function getRandomOpacity(start) {
    return start + (1-start)*Math.random();
}
function getRandomColor() {
    var colors = [
        [0, 0, 0],
        [1, 0.1+0.9*Math.random(), 1],
        [0.5, 0.1+0.9*Math.random(), 1],
        [0.1+0.9*Math.random(), 1, 1],
        [0.1+0.9*Math.random(), 0.5, 1],
        [0, 0, 0.1+0.9*Math.random()],                 
        /*[0.6, 1, 0.9*0.1*Math.random(), opacity], */

        [1, 0.1+0.9*Math.random(), 1],
        [0.5, 0.1+0.9*Math.random(), 1],
        [0.1+0.9*Math.random(), 1, 1],
        [0.1+0.9*Math.random(), 0.5, 1],
        [0, 0, 0.1+0.9*Math.random()],                 
        /*[0.6, 1, 0.9*0.1*Math.random(), opacity],*/

        [1, 0.1+0.9*Math.random(), 1],
        [0.5, 0.1+0.9*Math.random(), 1],
        [0.9+0.1*Math.random(), 1, 1],
        [0.9+0.1*Math.random(), 0.5, 1],
        [0, 0, 0.1+0.9*Math.random()],                 
        /*[0.6, 1, 0.9*0.1*Math.random(), opacity],*/
    ];
    var color = colors[Math.floor(Math.random()*colors.length)];
    return rgbToHex(Math.floor(color[0]*255), Math.floor(color[1]*255), Math.floor(color[2]*255));
}

function getFontNames(isForeGround){
    var fontNames = [];

    if (!isForeGround){
        if (doDouble){
            if (doCircle){
                fontNames.push('BitcountMonoDoubleRegularCircle');
                fontNames.push('BitcountMonoDoubleMediumCircle');
                fontNames.push('BitcountMonoDoubleBoldCircle');
            }
            if (doSquare){
                fontNames.push('BitcountMonoDoubleRegularSquare');
                fontNames.push('BitcountMonoDoubleMediumSquare');
                fontNames.push('BitcountMonoDoubleBoldSquare');
            }
        }
        if (doSingle){
            if (doCircle){
                fontNames.push('BitcountMonoSingleRegularCircle');
                fontNames.push('BitcountMonoSingleMediumCircle');
                fontNames.push('BitcountMonoSingleBoldCircle');
            }
            if (doSquare){
                fontNames.push('BitcountMonoSingleRegularSquare');
                fontNames.push('BitcountMonoSingleMediumSquare');
                fontNames.push('BitcountMonoSingleBoldSquare');
            }
        }
   }
    if (doDouble){
        if (doCircle){
            fontNames.push('BitcountMonoDoubleLightCircle');
            fontNames.push('BitcountMonoDoubleBookCircle');
        }
        if (doOpenCircle){
            fontNames.push('BitcountMonoDoubleLightLineCircle');
            fontNames.push('BitcountMonoDoubleBookLineCircle');
            fontNames.push('BitcountMonoDoubleRegularLineCircle');
            fontNames.push('BitcountMonoDoubleMediumLineCircle');
            fontNames.push('BitcountMonoDoubleBoldLineCircle');
        }
        if (doSquare){
            fontNames.push('BitcountMonoDoubleLightSquare');
            fontNames.push('BitcountMonoDoubleBookSquare');
        }
        if (doOpenSquare){
            fontNames.push('BitcountMonoDoubleLightLineSquare');
            fontNames.push('BitcountMonoDoubleBookLineSquare');
            fontNames.push('BitcountMonoDoubleRegularLineSquare');
            fontNames.push('BitcountMonoDoubleMediumLineSquare');
            fontNames.push('BitcountMonoDoubleBoldLineSquare');
        }
        if (doPlus){
            fontNames.push('BitcountMonoDoubleLightPlus');
            fontNames.push('BitcountMonoDoubleBookPlus');
            fontNames.push('BitcountMonoDoubleRegularPlus');
            fontNames.push('BitcountMonoDoubleMediumPlus');
            fontNames.push('BitcountMonoDoubleBoldPlus');
        }
    }
    if (doSingle){
        if (doCircle){
            fontNames.push('BitcountMonoSingleLightCircle');
            fontNames.push('BitcountMonoSingleBookCircle');
        }
        if (doOpenCircle){
            fontNames.push('BitcountMonoSingleLightLineCircle');
            fontNames.push('BitcountMonoSingleBookLineCircle');
            fontNames.push('BitcountMonoSingleRegularLineCircle');
            fontNames.push('BitcountMonoSingleMediumLineCircle');
            fontNames.push('BitcountMonoSingleBoldLineCircle');
        }
        if (doCircle){
            fontNames.push('BitcountMonoSingleLightSquare');
            fontNames.push('BitcountMonoSingleBookSquare');
        }
        if (doOpenSquare){
            fontNames.push('BitcountMonoSingleLightLineSquare');
            fontNames.push('BitcountMonoSingleBookLineSquare');
            fontNames.push('BitcountMonoSingleRegularLineSquare');
            fontNames.push('BitcountMonoSingleMediumLineSquare');
            fontNames.push('BitcountMonoSingleBoldLineSquare');
        }
        if (doPlus){
            fontNames.push('BitcountMonoSingleLightPlus');
            fontNames.push('BitcountMonoSingleBookPlus');
            fontNames.push('BitcountMonoSingleRegularPlus');
            fontNames.push('BitcountMonoSingleMediumPlus');
            fontNames.push('BitcountMonoSingleBoldPlus');
        }
    }
    /* Nothing selected, then select default. */
    if (fontNames.length == 0)
        fontNames.push('BitcountMonoDoubleRegularCircle');

    return fontNames;
}
function selectCircle(flag){
    if (flag == -1)
        flag = !doCircle;
    doCircle = flag;
    if (doCircle){
        document.getElementById('selectCircle').style['border'] = border;
        document.getElementById('selectNoCircle').style['border'] = 'none';
    } else {        
        document.getElementById('selectCircle').style['border'] = 'none';
        document.getElementById('selectNoCircle').style['border'] = border;
    }
    makeNewLayers();
}

function selectOpenCircle(flag){
    if (flag == -1)
        flag = !doOpenCircle;
    doOpenCircle = flag;
    if (doOpenCircle){
        document.getElementById('selectOpenCircle').style['border'] = border;
        document.getElementById('selectNoOpenCircle').style['border'] = 'none';
    } else {        
        document.getElementById('selectOpenCircle').style['border'] = 'none';
        document.getElementById('selectNoOpenCircle').style['border'] = border;
    }
    makeNewLayers();
}

function selectSquare(flag){
    if (flag == -1)
        flag = !doSquare;
    doSquare = flag;
    if (doSquare){
        document.getElementById('selectSquare').style['border'] = border;
        document.getElementById('selectNoSquare').style['border'] = 'none';
    } else {        
        document.getElementById('selectSquare').style['border'] = 'none';
        document.getElementById('selectNoSquare').style['border'] = border;
    }
    makeNewLayers();
}

function selectOpenSquare(flag){
   if (flag == -1)
        flag = !doOpenSquare;
    doOpenSquare = flag;
    if (doOpenSquare){
        document.getElementById('selectOpenSquare').style['border'] = border;
        document.getElementById('selectNoOpenSquare').style['border'] = 'none';
    } else {        
        document.getElementById('selectOpenSquare').style['border'] = 'none';
        document.getElementById('selectNoOpenSquare').style['border'] = border;
    }
    makeNewLayers();
}

function selectPlus(flag){
    if (flag == -1)
        flag = !doPlus;
    doPlus = flag;
    if (doPlus){
        document.getElementById('selectPlus').style['border'] = border;
        document.getElementById('selectNoPlus').style['border'] = 'none';
    } else {        
        document.getElementById('selectPlus').style['border'] = 'none';
        document.getElementById('selectNoPlus').style['border'] = border;
    }
    makeNewLayers();
}


function selectShift(flag){
    if (flag == -1)
        flag = !doShift;
    doShift = flag;
    if (doShift){
        document.getElementById('selectShift').style['border'] = border;
        document.getElementById('selectNoShift').style['border'] = 'none';
    } else {        
        document.getElementById('selectShift').style['border'] = 'none';
        document.getElementById('selectNoShift').style['border'] = border;
    }
    makeNewLayers();
}

function selectOpacity(flag){
    if (flag == -1)
        flag = !doOpacity;
    doOpacity = flag;
    if (doOpacity){
        document.getElementById('selectOpacity').style['border'] = border;
        document.getElementById('selectNoOpacity').style['border'] = 'none';
    } else {        
        document.getElementById('selectOpacity').style['border'] = 'none';
        document.getElementById('selectNoOpacity').style['border'] = border;
    }
    makeNewLayers();
}

function useShortSample(isShort){
    var s;
    if (isShort){
        // the width of browser is more then 991px
        s = 'Bit</br>';
    } else
        // the width of browser is less then 991px
        s = 'Bitcount</br>';

    document.getElementById('player1').innerHTML = s;
    document.getElementById('player2').innerHTML = s;
    document.getElementById('player3').innerHTML = s;
    document.getElementById('player4').innerHTML = s;
}

/* https://modernweb.com/using-media-queries-in-javascript/ */
var mq = window.matchMedia('all and (max-width: 991px)');
mq.addListener(function(changed) {
    useShortSample(changed.matches);
});

function selectStem(selectedStemType){
    if (selectedStemType == 'toggle'){
        doSingle = !doSingle;
        doDouble = !doDouble;
    } else if (selectedStemType == 'single'){
        doSingle = true;
        doDouble = false;
    } else if (selectedStemType == 'double'){
        doSingle = false;
        doDouble = true;
    } else { /* Mixes */
        doSingle = doDouble = true;
    }
    if (!(doSingle || doDouble))
        doSingle = true;
    if (doSingle && doDouble){
        document.getElementById('selectDouble').style['border'] = 'none';
        document.getElementById('selectSingle').style['border'] = 'none';
        document.getElementById('selectMix').style['border'] = border;
    } else if (doSingle){
        document.getElementById('selectDouble').style['border'] = 'none';
        document.getElementById('selectSingle').style['border'] = border;
        document.getElementById('selectMix').style['border'] = 'none';
    } else { /* doDouble */
        document.getElementById('selectDouble').style['border'] = border;
        document.getElementById('selectSingle').style['border'] = 'none';
        document.getElementById('selectMix').style['border'] = 'none';
    }
    stemType = selectedStemType;
    makeNewLayers();
}
function selectLayers(layers){
    document.getElementById('selectLayer1').style['border'] = 'none';
    document.getElementById('selectLayer2').style['border'] = 'none';
    document.getElementById('selectLayer3').style['border'] = 'none';
    document.getElementById('selectLayer4').style['border'] = 'none';
    if (layers == 0){
        layerCnt += 1;
        if (layerCnt > 4) layerCnt = 1;
    } else layerCnt = layers;
    document.getElementById('selectLayer'+layerCnt).style['border'] = border;
    makeNewLayers();
}
function toggleRomanItalic(){
    if (posture == 'normal'){
        posture = 'italic';
        document.getElementById('selectRoman').style['border'] = 'none';
        document.getElementById('selectItalic').style['border'] = border;
    } else { /* Italic */
        posture = 'normal'
        document.getElementById('selectRoman').style['border'] = border;
        document.getElementById('selectItalic').style['border'] = 'none';
    }
    makeNewLayers();
}
function makeNewLayers(){

    var fontNamesForeground = getFontNames(true);
    var fontNames = getFontNames(false);

    var css;
    var randomNumber1 = Math.floor(Math.random()*fontNamesForeground.length);
    var randomNumber2 = Math.floor(Math.random()*fontNamesForeground.length);
    var randomNumber3 = Math.floor(Math.random()*fontNames.length);
    var randomNumber4 = Math.floor(Math.random()*fontNames.length);

    var shifts = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,3,4,5,6];

    var e, c, f;
    var o = 1; /* In case no opacity */
    var x = 0;
    var y = 0;
    e = document.getElementById('playroom_content')
    /*e.style.lineHeight = Math.random()*0.02; /*0.0;*/

    e = document.getElementById('player1');
    e.style.color = c = getRandomColor();
    if (doOpacity)
        o = getRandomOpacity(0.8).toFixed(2);
    e.style.opacity = o;
    e.style.fontFamily = f = fontNamesForeground[randomNumber1];
    e.style.fontStyle = posture;
    if (doShift){
        x = shifts[Math.floor(Math.random()*shifts.length)];
        y = shifts[Math.floor(Math.random()*shifts.length)];
    }
    e.style.left = x+'px';
    e.style.top = y+'px';
    css = ".layer1 {font-family:"+f+"; style:"+posture+"; color:"+c+"; opacity:"+o+"; left:"+x+"px; top:"+y+"px;}<br>";

    e = document.getElementById('player2');
    e.style.color = c = getRandomColor();
    if (doOpacity)
        o = getRandomOpacity(0.8).toFixed(2);
    e.style.opacity = o;
    e.style.fontFamily = f = fontNamesForeground[randomNumber2];
    e.style.fontStyle = posture;
    if (layerCnt >= 2){
        if (doShift){
            x += shifts[Math.floor(Math.random()*shifts.length)];
            y += shifts[Math.floor(Math.random()*shifts.length)];
        }
        e.style.left = x+'px';
        e.style.top = y+'px';
        e.style.display = 'block';
        css += ".layer2 {font-family:"+f+"; style:"+posture+"; color:"+c+"; opacity:"+o+"; left:"+x+"px; top:"+y+"px;}<br>";
    } else
        e.style.display = 'none';
    
    e = document.getElementById('player3');
    e.style.color = c = getRandomColor();
    if (doOpacity)
        o = getRandomOpacity(0.6).toFixed(2);
    e.style.opacity = o;
    e.style.fontFamily = f = fontNames[randomNumber3];
    e.style.fontStyle = posture;
    if (layerCnt >= 3){
        if (doShift){
            x += shifts[Math.floor(Math.random()*shifts.length)];
            y += shifts[Math.floor(Math.random()*shifts.length)];
        }
        e.style.left = x+'px';
        e.style.top = y+'px';
        e.style.display = 'block';
        css += ".layer3 {font-family:"+f+"; style:"+posture+"; color:"+c+"; opacity:"+o+"; left:"+x+"px; top:"+y+"px;}<br>";
    } else
        e.style.display = 'none';
    
    e = document.getElementById('player4');
    e.style.color = c = getRandomColor();
    if (doOpacity)
        o = getRandomOpacity(0.6).toFixed(2);
    e.style.opacity = o;
    e.style.fontFamily = f = fontNames[randomNumber4];
    e.style.fontStyle = posture;
    if (layerCnt >= 4){
        if (doShift){
            x += shifts[Math.floor(Math.random()*shifts.length)];
            y += shifts[Math.floor(Math.random()*shifts.length)];
        }
        e.style.left = x+'px';
        e.style.top = y+'px';
        e.style.display = 'block';
        css += ".layer4 {font-family:"+f+"; style:"+posture+"; color:"+c+"; opacity:"+o+"; left:"+x+"px; top:"+y+"px;}<br>";
    } else
        e.style.display = 'none';

    document.getElementById('css_sample').innerHTML = css;
    document.getElementById('layerCnt').innerHTML = layerCnt;
};

useShortSample($(window).width() < 991);
toggleRomanItalic();
selectCircle(true);
selectOpenCircle(true);
selectSquare(true);
selectOpenSquare(true);
selectPlus(true);
selectOpacity(true);
selectShift(true);
selectStem('double');
selectLayers(4);
makeNewLayers();
