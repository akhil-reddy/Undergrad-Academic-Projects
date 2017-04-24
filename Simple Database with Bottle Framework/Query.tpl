<html>
<head>
<title>Player Display </title>
<style type="text/css">
	body{
		background-image: url('/Users/Reddy/pyprojects/larry.jpg');
	}
</style>
</head>
<body>
<h1>Players</h1>
<table>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>
</body>
</html>