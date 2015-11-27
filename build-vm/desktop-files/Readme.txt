=====================Readme=====================
NOTE: This is not the official README for Jalangi.
That is in the jalangi-src folder as README.md

NOTE: If ever necessary, the password for this VM
is "password".

This virtual machine is for basic interaction with the
Jalangi framework and its provided analyses. However,
keep in mind that Jalangi is no longer being maintained
and has degraded a bit since its initial release; not everything
is guaranteed to work, including some scripts on the official
README.md. Furthermore, the documentation has fallen out of date.
For the current version of Jalangi, visit the
page for Jalangi2 (https://github.com/Samsung/jalangi2).

The paper describes a number of ways to analyze javascript,
and the authors provided a number of premade analyses and test
files to explore them. To write your own, view the templates
in analysis.md and analysis2.md in the docs folder.

All scripts below should be executed in a terminal waiting in the 
jalangi-src directory:


================
Concolic Testing:

python scripts/jalangi.py concolic -i 100000 <test-file>
python scripts/jalangi.py rerunall <test-file>

For a list of prepared files, view concolic.txt on the desktop.
(Not all guaranteed to have error-free runs.)

NOTE: Do not include ".js" at the end of the filenames.
NOTE: At the end of the test generation, the output may include that
      the "test failed." However, I haven't yet been able to figure out
      any way anything has actually failed, so it seems unnecessary.

========================
Symbolic Test Generation:

python scripts/jalangi.py symbolic -i 100000 <test-file>

This function can use the same files as concolic testing. However,
it will not be able to use "rerunall" to run them. All tests will
still be visible in the "jalangi_tmp" folder after execution.

================
Dynamic Analyses:

python scripts/jalangi.py analyze -a <analysis-path> <file-path>

Premade Analysis Paths:
	Tracking Null and Undefined:	src/js/analyses/trackundefinednull/UndefinedNullTrackingEngine
	Likely Type Inconsistencies:	src/js/analyses/likelytype/LikelyTypeInferEngine
	Object Allocation Profiler:	src/js/analyses/objectalloc/ObjectAllocationTrackerEngine
	Dynamic Taint Analysis:	 	src/js/analyses/simpletaint/SimpleTaintEngine

These can be run on any javascript file in the tests folder. To see
it in action, you can try it them on some of the files in the sunspider1
folder, as well as other test folders in that same directory (such as "unit"):

	python scripts/jalangi.py analyze -a src/js/analyses/objectalloc/ObjectAllocationTrackerEngine tests/sunspider1/crypto-aes
	python scripts/jalangi.py analyze -a src/js/analyses/likelytype/LikelyTypeInferEngine tests/sunspider1/crypto-sha1

NOTE: In choosing a test file, do not include the ".js" at the end of its name.
      Also, avoid the files that end with "_jalangi_.js", as they are the 
      instrumented versions of the similarly named files.



==========
The below two options are for running javascript apps in browsers. This VM
is equipped with both Firefox and Chromium. Jalangi should work with either,
but you may find that errors using one will not arise using the other.

If you wish to switch which is loaded by default, navigate to System Settings
by clicking the options menu in the top-right corner. In the search bar, search
for and double-click "Details." The "Default Applications" menu there lets you
set your default web browser.

Sample javascript apps can be found in tests/tizen. Not all are guaranteed to work.
The app "annex" is a good one to start with and will be used in the examples.

=====================================
Recording/Replaying a Web Application:

	node src/js/commands/instrument.js --outputDir /tmp tests/tizen/annex
	killall node
	python scripts/jalangi.py rrserver file:///tmp/annex/index.html

	(At this point, the browser launches. Play for a bit, then flush the trace
	by pressing "Alt+Shift+T," then close the browser.)

	cp jalangi_trace1 /tmp/annex
	node src/js/commands/replay.js --tracefile /tmp/annex/jalangi_trace1 --analysis <analysis-path>

The analysis paths are the same as the ones in the Dynamic Analysis section.

===================
In-Browser Analysis:
	node src/js/commands/instrument.js --inbrowser --smemory --analysis <IB-analysis-path> --outputDir /tmp tests/tizen/annex
	xdg-open file:///tmp/annex/index.html (or navigate to the file location in a browser)

	(First, open the browser console by pressing "Ctrl+Shift+J".
	 After a few moves, you can view the output by pressing "Alt-Shift-T".)

For the analysis here, you will need to use ones specifically
designed for In-Browser analysis (and include the ".js"), which includes:

	src/js/analyses/likelytype/LikelyTypeInferEngineIB.js
	src/js/analyses/objectalloc/ObjectAllocationTrackerEngineIB.js


====================
