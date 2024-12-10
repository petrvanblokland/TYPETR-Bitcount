## FontBakery report

fontbakery version: 0.12.8



## Experimental checks

These won't break the CI job for now, but will become effective after some time if nobody raises any concern.


<details><summary>[2] BitcountGridSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountGridDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 💥 **ERROR** <p>Failed with AttributeError: 'NoneType' object has no attribute 'LookupType'</p>
<pre><code>  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checkrunner.py&quot;, line 209, in _run_check
    subresults = check(**args)  # Might raise.
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/callable.py&quot;, line 99, in __call__
    return self.__wrapped__(*args, **kwds)
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checks/universal/__init__.py&quot;, line 1234, in com_google_fonts_check_gsub_smallcaps_before_ligatures
    lookup_order = {
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checks/universal/__init__.py&quot;, line 1235, in &lt;dictcomp&gt;
    lookup.LookupType: idx

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 💥 **ERROR** <p>Failed with AttributeError: 'NoneType' object has no attribute 'LookupType'</p>
<pre><code>  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checkrunner.py&quot;, line 209, in _run_check
    subresults = check(**args)  # Might raise.
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/callable.py&quot;, line 99, in __call__
    return self.__wrapped__(*args, **kwds)
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checks/universal/__init__.py&quot;, line 1234, in com_google_fonts_check_gsub_smallcaps_before_ligatures
    lookup_order = {
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checks/universal/__init__.py&quot;, line 1235, in &lt;dictcomp&gt;
    lookup.LookupType: idx

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountPropDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountPropSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>

<details><summary>[2] BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' lookups are not defined before 'liga' lookups.</p>
 [code: feature-ordering]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>




## All other checks



<details><summary>[4] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Fonts have consistent underline thickness? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.post.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Thickness of the underline is not the same across this family. In order to fix this, please make sure that the underlineThickness value is the same in the 'post' table of all of this family font files.
Detected underlineThickness values are:
fonts/ttf/variable/BitcountGridSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf: 50
fonts/ttf/variable/BitcountGridDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf: 50
fonts/ttf/variable/BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: 50
fonts/ttf/variable/BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: 50
fonts/ttf/variable/BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: 50
fonts/ttf/variable/BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: 50
fonts/ttf/variable/BitcountPropDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf: 50
fonts/ttf/variable/Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf: 100
fonts/ttf/variable/BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf: 100
fonts/ttf/variable/BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: 50
fonts/ttf/variable/BitcountPropSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf: 50
fonts/ttf/variable/BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf: 50</p>
 [code: inconsistent-underline-thickness]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>12 different Font Family names were found:</p>
<ul>
<li>
<p>'Bitcount Grid Single Ink' was found in:</p>
<ul>
<li>BitcountGridSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Grid Double Ink' was found in:</p>
<ul>
<li>BitcountGridDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Mono Single' was found in:</p>
<ul>
<li>BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Grid Double' was found in:</p>
<ul>
<li>BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Grid Single' was found in:</p>
<ul>
<li>BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Prop Single' was found in:</p>
<ul>
<li>BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Prop Double Ink' was found in:</p>
<ul>
<li>BitcountPropDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount' was found in:</p>
<ul>
<li>Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Mono Double Ink' was found in:</p>
<ul>
<li>BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Prop Double' was found in:</p>
<ul>
<li>BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Prop Single Ink' was found in:</p>
<ul>
<li>BitcountPropSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Bitcount Mono Single Ink' was found in:</p>
<ul>
<li>BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf (nameID 1)</li>
</ul>
</li>
</ul>
 [code: inconsistent-family-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check that family axis ranges are indentical <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Variable axes ranges not matching between font files</p>
 [code: axis-range-mismatch]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure that all variable font files have the same set of axes and axis ranges. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN1' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'SZP2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'XPN2' variation axis.</p>
 [code: missing-axis]



* 🔥 **FAIL** <p>BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf: lacks a 'YPN2' variation axis.</p>
 [code: missing-axis]



</div>
</details>
</div>
</details>

<details><summary>[14] BitcountGridSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1187 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 14 glyphs (1.18%) have a different width. You should check the widths of: ['canvas', 'px', 'fi', 'fl', 'fi.it', 'fl.it', 'fi.cd_it', 'fl.cd_it', 'fi.sc', 'fl.sc', 'fi.sc_cd', 'fl.sc_cd', 'fi.cd', 'fl.cd']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0145: LATIN CAPITAL LETTER N WITH CEDILLA</td>
<td align="left">U+0146: LATIN SMALL LETTER N WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lv_Latn (Latvian)</td>
<td align="left">Shaper didn't attach cedillacomb to n</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Grid Single Ink ExtraLight' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 267 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Grid Single Ink SemiBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 271 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Grid Single Ink ExtraBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 273 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* ⚠️ **WARN** <p>Name ID 6 'BitcountGridSingleInk-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms.</p>
 [code: nameid6-too-long]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.cd

- Germandbls.ct

- Germandbls.sc

- dslash

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_five_circles

- el_hstripe

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- fi.sc

- fi.sc_cd

- fl.sc

- fl.sc_cd

- idotaccent

- jdotless.cd

- jdotless.xd

- jdotless.xd_cd

- ncommaaccent

- uni00A0
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[13] BitcountGridDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 💥 **ERROR** <p>Failed with AttributeError: 'NoneType' object has no attribute 'LookupType'</p>
<pre><code>  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checkrunner.py&quot;, line 213, in _run_check
    subresults = list(subresults)
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checks/universal/glyphset.py&quot;, line 248, in com_google_fonts_check_unreachable_glyphs
    remove_lookup_outputs(all_glyphs, lookup)
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checks/universal/glyphset.py&quot;, line 111, in remove_lookup_outputs
    if lookup.LookupType == 1:  # Single:

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 709 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 8 glyphs (1.13%) have a different width. You should check the widths of: ['canvas', 'px', 'fi', 'fl', 'fi.it', 'fl.it', 'fi.sc', 'fl.sc']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking with ots-sanitize. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.sanitize.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>ots-sanitize returned an error code (1). Output follows:</p>
<p>ERROR: GSUB: Bad lookup offset 0 for lookup 0
ERROR: GSUB: Failed to parse lookup list table
ERROR: GSUB: Failed to parse table
Failed to sanitize file!</p>
 [code: ots-sanitize-error]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Grid Double Ink ExtraLight' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 265 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Grid Double Ink SemiBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 269 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Grid Double Ink ExtraBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 271 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* ⚠️ **WARN** <p>Name ID 6 'BitcountGridDoubleInk-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms.</p>
 [code: nameid6-too-long]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[15] BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1754 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 38 glyphs (2.17%) have a different width. You should check the widths of: ['canvas', 'px', 'fi', 'fl', 'fi.xa_cd', 'fl.xa_cd', 'fi.xd', 'fl.xd', 'fi.xd_cd', 'fl.xd_cd', 'fi.it', 'fl.it', 'fi.cd_it', 'fl.cd_it', 'fi.xa_xd', 'fl.xa_xd', 'fi.xa_xd_cd', 'fl.xa_xd_cd', 'fi.xa_it', 'fl.xa_it', 'fi.xd_it', 'fl.xd_it', 'fi.xa_cd_it', 'fl.xa_cd_it', 'fi.xa_xd_it', 'fl.xa_xd_it', 'fi.xd_cd_it', 'fl.xd_cd_it', 'fi.xa_xd_cd_it', 'fl.xa_xd_cd_it', 'fi.xa', 'fl.xa', 'fi.sc', 'fl.sc', 'fi.sc_cd', 'fl.sc_cd', 'fi.cd', 'fl.cd']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0145: LATIN CAPITAL LETTER N WITH CEDILLA</td>
<td align="left">U+0146: LATIN SMALL LETTER N WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lv_Latn (Latvian)</td>
<td align="left">Shaper didn't attach cedillacomb to n</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;BitcountMonoSingle[CRSV,ELSH,ELXP,slnt,wght].ttf. Got BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf.</p>
 [code: bad-filename]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.cd

- Germandbls.ct

- Germandbls.sc

- Germandbls.xa

- Germandbls.xa_cd

- Germandbls.xa_ct

- dcroat.xa_ct

- dslash

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_diamond

- el_five_circles

- el_hstripe

- el_raster

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_star

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- fi.sc_cd

- five.lc_xd_ct

- fl.sc_cd

- four.lc_xd

- idotaccent

- jdotless.cd

- jdotless.xd

- jdotless.xd_cd

- ncommaaccent

- nine.lc_xd

- seven.lc_xd

- three.lc_xd

- uni00A0
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̇ ǐ i̦̇ i̦̊ i̦̋ ǐ̦ i̧̇ i̧̊ i̧̋ ǐ̧ j̆ j̇ j̊ j̋ ǰ j̦̀ j̦́ j̦̃ j̦̄ j̦̆</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Basaa (Latn, 332,940 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Navajo (Latn, 166,319 speakers), Igbo (Latn, 27,823,640 speakers), Belarusian (Cyrl, 10,064,517 speakers), Aghem (Latn, 38,843 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[12] BitcountGridDouble[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 💥 **ERROR** <p>Failed with AttributeError: 'NoneType' object has no attribute 'LookupType'</p>
<pre><code>  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checkrunner.py&quot;, line 213, in _run_check
    subresults = list(subresults)
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checks/universal/glyphset.py&quot;, line 248, in com_google_fonts_check_unreachable_glyphs
    remove_lookup_outputs(all_glyphs, lookup)
  File &quot;/home/runner/work/TYPETR-Bitcount/TYPETR-Bitcount/venv/lib/python3.10/site-packages/fontbakery/checks/universal/glyphset.py&quot;, line 111, in remove_lookup_outputs
    if lookup.LookupType == 1:  # Single:

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 709 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 8 glyphs (1.13%) have a different width. You should check the widths of: ['canvas', 'px', 'fi', 'fl', 'fi.it', 'fl.it', 'fi.sc', 'fl.sc']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking with ots-sanitize. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.sanitize.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>ots-sanitize returned an error code (1). Output follows:</p>
<p>ERROR: GSUB: Bad lookup offset 0 for lookup 0
ERROR: GSUB: Failed to parse lookup list table
ERROR: GSUB: Failed to parse table
Failed to sanitize file!</p>
 [code: ots-sanitize-error]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[13] BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1187 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 14 glyphs (1.18%) have a different width. You should check the widths of: ['canvas', 'px', 'fi', 'fl', 'fi.it', 'fl.it', 'fi.cd_it', 'fl.cd_it', 'fi.sc', 'fl.sc', 'fi.sc_cd', 'fl.sc_cd', 'fi.cd', 'fl.cd']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0145: LATIN CAPITAL LETTER N WITH CEDILLA</td>
<td align="left">U+0146: LATIN SMALL LETTER N WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lv_Latn (Latvian)</td>
<td align="left">Shaper didn't attach cedillacomb to n</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.cd

- Germandbls.ct

- Germandbls.sc

- dslash

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_diamond

- el_five_circles

- el_hstripe

- el_raster

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_star

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- fi.sc

- fi.sc_cd

- fl.sc

- fl.sc_cd

- idotaccent

- jdotless.cd

- jdotless.xd

- jdotless.xd_cd

- ncommaaccent

- uni00A0
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[11] Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1044 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 21 glyphs (2.01%) have a different width. You should check the widths of: ['canvas', 'px', 'fi', 'fl', '_canvas', 'fi.xd', 'fl.xd', 'fi.it', 'fl.it', 'fi.xa_xd', 'fl.xa_xd', 'fi.xa_it', 'fl.xa_it', 'fi.xd_it', 'fl.xd_it', 'fi.xa_xd_it', 'fl.xa_xd_it', 'fi.xa', 'fl.xa', 'fi.sc', 'fl.sc']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.sc

- chess

- chesssquare

- circle

- circle_large

- circles

- diamond

- dslash

- eight.lc

- eight.lc_xc

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_diamond

- el_five_circles

- el_hstripe

- el_raster

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_star

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- five.lc

- five_circles

- four.lc

- four.lc_xd

- hstripe

- i.trk

- idotaccent

- jdotless.xd

- mt

- nine.lc

- nine.lc_xd

- one.lc

- raster

- rastersquare

- seven.lc

- seven.lc_xd

- six.lc

- six.lc_xc

- square

- square_large

- squares

- squares2

- star

- three.lc

- three.lc_xd

- triangle

- two.lc

- uni00A0

- vstripe

- vzigzag

- zero.lc

- zigzag
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[13] BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1044 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 21 glyphs (2.01%) have a different width. You should check the widths of: ['canvas', 'px', 'fi', 'fl', '_canvas', 'fi.xd', 'fl.xd', 'fi.it', 'fl.it', 'fi.xa_xd', 'fl.xa_xd', 'fi.xa_it', 'fl.xa_it', 'fi.xd_it', 'fl.xd_it', 'fi.xa_xd_it', 'fl.xa_xd_it', 'fi.xa', 'fl.xa', 'fi.sc', 'fl.sc']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Mono Double Ink ExtraLight' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 268 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Mono Double Ink SemiBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 272 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Mono Double Ink ExtraBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 274 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* ⚠️ **WARN** <p>Name ID 6 'BitcountMonoDoubleInk-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms.</p>
 [code: nameid6-too-long]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;BitcountMonoDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf. Got BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf.</p>
 [code: bad-filename]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.sc

- chess

- chesssquare

- circle

- circle_large

- circles

- diamond

- dslash

- eight.lc

- eight.lc_xc

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_five_circles

- el_hstripe

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- five.lc

- five_circles

- four.lc

- four.lc_xd

- hstripe

- i.trk

- idotaccent

- jdotless.xd

- mt

- nine.lc

- nine.lc_xd

- one.lc

- raster

- rastersquare

- seven.lc

- seven.lc_xd

- six.lc

- six.lc_xc

- square

- square_large

- squares

- squares2

- star

- three.lc

- three.lc_xd

- triangle

- two.lc

- uni00A0

- vstripe

- vzigzag

- zero.lc

- zigzag
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[16] BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1754 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 38 glyphs (2.17%) have a different width. You should check the widths of: ['canvas', 'px', 'fi', 'fl', 'fi.xa_cd', 'fl.xa_cd', 'fi.xd', 'fl.xd', 'fi.xd_cd', 'fl.xd_cd', 'fi.it', 'fl.it', 'fi.cd_it', 'fl.cd_it', 'fi.xa_xd', 'fl.xa_xd', 'fi.xa_xd_cd', 'fl.xa_xd_cd', 'fi.xa_it', 'fl.xa_it', 'fi.xd_it', 'fl.xd_it', 'fi.xa_cd_it', 'fl.xa_cd_it', 'fi.xa_xd_it', 'fl.xa_xd_it', 'fi.xd_cd_it', 'fl.xd_cd_it', 'fi.xa_xd_cd_it', 'fl.xa_xd_cd_it', 'fi.xa', 'fl.xa', 'fi.sc', 'fl.sc', 'fi.sc_cd', 'fl.sc_cd', 'fi.cd', 'fl.cd']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0145: LATIN CAPITAL LETTER N WITH CEDILLA</td>
<td align="left">U+0146: LATIN SMALL LETTER N WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lv_Latn (Latvian)</td>
<td align="left">Shaper didn't attach cedillacomb to n</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Mono Single Ink ExtraLight' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 269 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Mono Single Ink SemiBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 273 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Mono Single Ink ExtraBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 275 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* ⚠️ **WARN** <p>Name ID 6 'BitcountMonoSingleInk-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms.</p>
 [code: nameid6-too-long]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;BitcountMonoSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf. Got BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf.</p>
 [code: bad-filename]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.cd

- Germandbls.ct

- Germandbls.sc

- Germandbls.xa

- Germandbls.xa_cd

- Germandbls.xa_ct

- dcroat.xa_ct

- dslash

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_five_circles

- el_hstripe

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- fi.sc_cd

- five.lc_xd_ct

- fl.sc_cd

- four.lc_xd

- idotaccent

- jdotless.cd

- jdotless.xd

- jdotless.xd_cd

- ncommaaccent

- nine.lc_xd

- seven.lc_xd

- three.lc_xd

- uni00A0
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̇ ǐ i̦̇ i̦̊ i̦̋ ǐ̦ i̧̇ i̧̊ i̧̋ ǐ̧ j̆ j̇ j̊ j̋ ǰ j̦̀ j̦́ j̦̃ j̦̄ j̦̆</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Basaa (Latn, 332,940 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Navajo (Latn, 166,319 speakers), Igbo (Latn, 27,823,640 speakers), Belarusian (Cyrl, 10,064,517 speakers), Aghem (Latn, 38,843 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[14] BitcountPropSingle[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check glyphs do not have duplicate components which have the same x,y coordinates. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.glyf.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs have duplicate components which have the same x,y coordinates:
* {'glyph': 'Dcircle', 'component': 'px', 'x': 200, 'y': 400}</p>
 [code: found-duplicates]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0145: LATIN CAPITAL LETTER N WITH CEDILLA</td>
<td align="left">U+0146: LATIN SMALL LETTER N WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lv_Latn (Latvian)</td>
<td align="left">Shaper didn't attach cedillacomb to n</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 10 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
plusminus, lessequal, greaterequal</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.cd

- Germandbls.ct

- Germandbls.sc

- Germandbls.sc_cd

- Germandbls.xa

- Germandbls.xa_cd

- Germandbls.xa_ct

- dslash

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_diamond

- el_five_circles

- el_hstripe

- el_raster

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_star

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- five.lc_xd_ct

- four.lc_xd

- idotaccent

- jdotless.xd

- ncommaaccent

- nine.lc_xd

- seven.lc_xd

- three.lc_xd

- uni00A0
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Is there kerning info for non-ligated sequences? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning info for the following non-ligated sequences:</p>
<pre><code>- f + i

- f + l
</code></pre>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[15] BitcountPropSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check glyphs do not have duplicate components which have the same x,y coordinates. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.glyf.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs have duplicate components which have the same x,y coordinates:
* {'glyph': 'Dcircle', 'component': 'px', 'x': 200, 'y': 400}</p>
 [code: found-duplicates]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0145: LATIN CAPITAL LETTER N WITH CEDILLA</td>
<td align="left">U+0146: LATIN SMALL LETTER N WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lv_Latn (Latvian)</td>
<td align="left">Shaper didn't attach cedillacomb to n</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Prop Single Ink ExtraLight' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 269 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Prop Single Ink SemiBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 273 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Prop Single Ink ExtraBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 275 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* ⚠️ **WARN** <p>Name ID 6 'BitcountPropSingleInk-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms.</p>
 [code: nameid6-too-long]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 10 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
plusminus, lessequal, greaterequal</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.cd

- Germandbls.ct

- Germandbls.sc

- Germandbls.sc_cd

- Germandbls.xa

- Germandbls.xa_cd

- Germandbls.xa_ct

- dslash

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_five_circles

- el_hstripe

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- five.lc_xd_ct

- four.lc_xd

- idotaccent

- jdotless.xd

- ncommaaccent

- nine.lc_xd

- seven.lc_xd

- three.lc_xd

- uni00A0
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Is there kerning info for non-ligated sequences? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning info for the following non-ligated sequences:</p>
<pre><code>- f + i

- f + l
</code></pre>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[12] BitcountPropDoubleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Prop Double Ink ExtraLight' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 268 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Prop Double Ink SemiBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 272 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Bitcount Prop Double Ink ExtraBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 274 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* ⚠️ **WARN** <p>Name ID 6 'BitcountPropDoubleInk-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms.</p>
 [code: nameid6-too-long]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5, SZP1=30.0, XPN1=50.0, YPN1=50.0, SZP2=30.0, XPN2=50.0, YPN2=50.0</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 12 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
plusminus</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.sc

- dslash

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_five_circles

- el_hstripe

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- f.xd_it

- fi.xd_it

- four.lc_xd

- i.trk

- idotaccent

- jdotless.xd

- nine.lc_xd

- seven.lc_xd

- three.lc_xd

- uni00A0
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Is there kerning info for non-ligated sequences? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning info for the following non-ligated sequences:</p>
<pre><code>- f + i

- f + l
</code></pre>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[11] BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.12.8, while a newer 0.12.10 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>fvar instances are incorrect:</p>
<ul>
<li>Add missing instances</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Thin Italic</td>
<td align="left">N/A</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Thin</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=100.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight Italic</td>
<td align="left">N/A</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraLight</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=200.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light Italic</td>
<td align="left">N/A</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Light</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=300.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Italic</td>
<td align="left">N/A</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Regular</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=400.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium Italic</td>
<td align="left">N/A</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Medium</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=500.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">SemiBold</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=600.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Bold</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=700.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold Italic</td>
<td align="left">N/A</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">ExtraBold</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=800.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black Italic</td>
<td align="left">N/A</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=-8.0, CRSV=0.5</td>
</tr>
<tr>
<td align="left">Black</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
<td align="left">wght=900.0, ELXP=0.0, ELSH=0.0, slnt=0.0, CRSV=0.5</td>
</tr>
</tbody>
</table>
 [code: bad-fvar-instances]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 12 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
plusminus</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- Germandbls.sc

- dslash

- el_chess

- el_chesssquare

- el_circle

- el_circle_large

- el_circles

- el_diamond

- el_five_circles

- el_hstripe

- el_raster

- el_rastersquare

- el_square

- el_square_large

- el_squares

- el_squares2

- el_star

- el_triangle

- el_vstripe

- el_vtriangle

- el_vzigzag

- el_zigzag

- f.xd_it

- fi.xd_it

- four.lc_xd

- i.trk

- idotaccent

- jdotless.xd

- nine.lc_xd

- seven.lc_xd

- three.lc_xd

- uni00A0
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, canadian-aboriginal, syriac, tifinagh, old-permic, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+F8FF : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">WARN messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
<td align="left">No exemplar glyphs were defined for language Norwegian Bokmål</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Is there kerning info for non-ligated sequences? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning info for the following non-ligated sequences:</p>
<pre><code>- f + i

- f + l
</code></pre>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 4 | 0 | 77 | 106 | 1076 | 85 | 1406 | 0 | 
| 0% | 0% | 3% | 4% | 39% | 3% | 51% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
