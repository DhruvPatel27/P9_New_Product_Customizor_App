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
    <h2>Account Details</h2>
	   <table>
		   <tr>
			  <td>
				  <div class="label">Name <br/></div>
			   </td>
			   
			   <td>
				   <div id="vertLine"/>
			   </td>
			   <td>
				  <div id="history"class="label">Order History<br/></div>
			   </td>
		   </tr>
		   <tr>
			  <td>
				  <div class="label">Primary Address <br/></div>
			   </td>
			   <td>
				   <div id="vertLine"/>
			   </td>
		   </tr>
	   </table>
	  <div id="logout"><input type="submit" class="submit" value="Logout"></div><br/>
  </section>
  <div id="content"> </div></div>
</body>
</html>
