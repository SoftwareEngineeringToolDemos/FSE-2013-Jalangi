=====================Readme=====================
To see the official README, view the README.md in the source
folder. For the currently maintained version of Jalangi, visit the
page for Jalangi2 (https://github.com/Samsung/jalangi2).

To write your own analyses, view the templates
in analysis.md and analysis2.md in the docs folder.

All scripts below should be executed in a terminal waiting in the 
FSE-2013-Jalangi directory:

================
Concolic Testing:

	python scripts/jalangi.py concolic -i 100000 <test-file>
	python scripts/jalangi.py rerunall <test-file>

View "concolic.txt" on the desktop for a list of sample files.
NOTE: Do not include ".js" at the end of the filenames.

Example:

	python scripts/jalangi.py concolic -i 100000 tests/unit/qsort
        python scripts/jalangi.py rerunall tests/unit/qsort

========================
Symbolic Test Generation:

	python scripts/jalangi.py symbolic -i 100000 <test-file>

View "concolic.txt" for sample files. For these, "rerunall" won't work, 
but the tests will be visible in the "jalangi_tmp" folder.

================
Dynamic Analyses:

	python scripts/jalangi.py analyze -a <analysis-path> <file-path>

Analysis Paths (premade):
	Tracking Null and Undefined:	src/js/analyses/trackundefinednull/UndefinedNullTrackingEngine
	Likely Type Inconsistencies:	src/js/analyses/likelytype/LikelyTypeInferEngine
	Object Allocation Profiler:	src/js/analyses/objectalloc/ObjectAllocationTrackerEngine
	Dynamic Taint Analysis:	 	src/js/analyses/simpletaint/SimpleTaintEngine

These can be run on any javascript file in the tests folder. View
"sunspider.txt" for sample files, as well as other test folders 
in that same directory (such as "unit"):

	python scripts/jalangi.py analyze -a src/js/analyses/objectalloc/ObjectAllocationTrackerEngine tests/sunspider1/crypto-aes
	python scripts/jalangi.py analyze -a src/js/analyses/likelytype/LikelyTypeInferEngine tests/sunspider1/crypto-sha1

NOTE: In choosing a test file, do not include the ".js" at the end of its name.
      Also, avoid the files that end with "_jalangi_.js", as they are the 
      instrumented versions of the similarly named files.



==========
The below two options are for running javascript apps in browsers. This VM
is equipped with both Firefox and Chromium. Jalangi should work with either,
but you may find that errors using one will not arise using the other.

To switch default browsers:
	1. Navigate to System Settings by clicking the options menu in the top-right corner. 
	2. In the search bar, search for and double-click "Details." 
	3. Set default browser in the "Default Applications" menu.

See "tests/tizen" for sample javascript apps, specifically "annex" (which I've filled in
in the examples below). Some of the others have degraded and won't work as intended.

=====================================
Recording/Replaying a Web Application:
Enter the following commands in the terminal:

	node src/js/commands/instrument.js --outputDir /tmp tests/tizen/annex
	killall node
	python scripts/jalangi.py rrserver file:///tmp/annex/index.html

	(At this point, the browser launches. Play for a bit, then flush the trace
	by pressing "Alt+Shift+T," then close the browser.)

	cp jalangi_trace1 /tmp/annex
	node src/js/commands/replay.js --tracefile /tmp/annex/jalangi_trace1 --analysis <analysis-path>

The analysis paths are the same as the ones in the "Dynamic Analysis" section.

===================
In-Browser Analysis:
	node src/js/commands/instrument.js --inbrowser --smemory --analysis <IB-analysis-path> --outputDir /tmp tests/tizen/annex
	xdg-open file:///tmp/annex/index.html (or navigate to the file location in a browser)

	(First, open the browser console by pressing "Ctrl+Shift+J".
	 After a few moves, you can view the output by pressing "Alt-Shift-T".)

IB Analysis Paths:
	src/js/analyses/likelytype/LikelyTypeInferEngineIB.js
	src/js/analyses/objectalloc/ObjectAllocationTrackerEngineIB.js


====================
