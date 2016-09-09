<!DOCTYPE html>
<html lang="en">
<head>
<title>Kuhn TV Generator</title>
<link rel="stylesheet" href="lib/jquery-ui.min.css">
<link href="css/normalize.css" rel="stylesheet">
<link href="css/tv.css" rel="stylesheet">
</head>
<body>
	<h1>Kuhn TV Generator</h1>
	Date: <input type="text" id="tv-start"> to <input type="text" id="tv-end"><br><br>
	<div id="buttons">
		<input type="button" id="gen" value="Generate">
		<input type="button" id="down" value="Download"/>
		<input type="button" id="reset" value="Reset"/>
	</div><br>
	<form id='tv-output-form' method='post' action='tv.jpg' target='_blank' >
		<div id="output">
		</div>
	</form>
	<div id="reset-dialog" title="Reset Generator" style="display:none;">
		<p><span class="ui-icon ui-icon-alert icon-attn"></span>Are you sure you want to reset the entire generator?</p>
	</div>
	<div id="download-dialog" title="Download" style="display:none;">
		<form id='tv-output-form-dl' method='post' action='tv.jpg' target='_blank'>
		</form>
	</div>

	<script src="lib/jquery.min.js"></script>
	<script src="lib/jquery-ui.min.js"></script>
	<script src="lib/moment.js"></script>
	<script src="tv.js"></script>
</body>
<!--
Started 6:30p on 9/7

-->
</html>	