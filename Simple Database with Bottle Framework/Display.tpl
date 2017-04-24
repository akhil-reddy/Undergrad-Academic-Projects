<html>
<head>
<title>Player Display </title>
<style type="text/css">
	body{
		background-image: url('/Users/Reddy/pyprojects/larry.jpg');
	}
	@import "compass/css3";

@import "compass/css3";
@import url(http://fonts.googleapis.com/css?family=Patua+One|Open+Sans);

* { 
  -moz-box-sizing: border-box; 
  -webkit-box-sizing: border-box; 
	box-sizing: border-box; 
}

body {
  background:#353a40;
}

table {
  border-collapse: separate;
  background:#fff;
  @include border-radius(5px);
  margin:50px auto;
  @include box-shadow(0px 0px 5px rgba(0,0,0,0.3));
}

thead {
  @include border-radius(5px);
}

thead th {
  font-family: 'Patua One', cursive;
  font-size:16px;
  font-weight:400;
  color:#fff;
  @include text-shadow(1px 1px 0px rgba(0,0,0,0.5));
  text-align:left;
  padding:20px;
  @include background-image(linear-gradient(#646f7f, #4a5564));
  border-top:1px solid #858d99;
  
  &:first-child {
   @include border-top-left-radius(5px); 
  }

  &:last-child {
    @include border-top-right-radius(5px); 
  }
}

tbody tr td {
  font-family: 'Open Sans', sans-serif;
  font-weight:400;
  color:#5f6062;
  font-size:13px;
  padding:20px 20px 20px 20px;
  border-bottom:1px solid #e0e0e0;
  
}

tbody tr:nth-child(2n) {
  background:#f0f3f5;
}

tbody tr:last-child td {
  border-bottom:none;
  &:first-child {
    @include border-bottom-left-radius(5px);
  }
  &:last-child {
    @include border-bottom-right-radius(5px);
  }
}

tbody:hover > tr td {
  @include opacity(0.5);
  
  /* uncomment for blur effect */
  /* color:transparent;
  @include text-shadow(0px 0px 2px rgba(0,0,0,0.8));*/
}

tbody:hover > tr:hover td {
  @include text-shadow(none);
  color:#2d2d2d;
  @include opacity(1.0);
}

</style>
</head>
<body>
<h1 align="center">Players</h1>
<table>
<tr><th>Player ID</th><th>First Name</th><th>Last Name</th><th>DoB</th><th>Height</th><th>Weight</th><th>Team ID</th></tr>
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