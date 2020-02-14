<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="CSS/login.css" rel="stylesheet" type="text/css">
	<!--The following script tag downloads a font from the Adobe Edge Web Fonts server for use within the web page. We recommend that you do not modify it.-->
	<script>var __adobewebfontsappname__="dreamweaver"</script>
	<script src="http://use.edgefonts.net/montserrat:n4:default;source-sans-pro:n2:default.js" type="text/javascript"></script>
</head>
<jsp:include page="basic-layout.jsp"></jsp:include>

<body>
<div id="mainWrapper">
   <section id="login"> 
    <!-- The offer section displays a banner text for promotions -->
    <h2>Customer Login</h2>
	  <div class="label">Email ID: </div>
	  <div><input class="text" type="text" name="username"><br/></div>
	  <div class="label">Password: </div>
	  <div><input class="text" type="password" name="password"><br/><br/></div>
	  <div><input type="submit" class="submit" value="Login"></div><br/>
	  <div> New Customer? <a href="Signup.jsp" class="link">Signup</a> </div>
  </section>
  <div id="content"> </div></div>
</body>

</body>
</html>
