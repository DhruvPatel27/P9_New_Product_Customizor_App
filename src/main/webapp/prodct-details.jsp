<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Simple Theme</title>
<link href="CSS/product-details.css" rel="stylesheet" type="text/css">
</head>
<body>
<jsp:include page="basic-layout.jsp" /> 
<div class="container">
  <section>
    <h2 class="noDisplay">Main Content</h2> 
    <aside class="left_article"><img src="../webapp/images/image.jpeg" alt="" width="400" height="200" class="placeholder"/> </aside>
    <article class="right_article">
      <h3 font-size:20px ><strong>iPhone XR Case</strong></h3>
	  <h3><strong>$25.00</strong></h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
		
		<h3>Select Wood type</h3>
		<h3>
		<button class="wood_select_buttons cherry" title="Cherry" ></button>
		<button class="wood_select_buttons oak" title="Oak"></button>
		<button class="wood_select_buttons maple" title="Maple"></button>
		<button class="wood_select_buttons pine" title="Pine"></button>
		<button class="wood_select_buttons walnut" title="Walnut"></button>
        </h3>
		<h3>Enter personal message</h3>
		<h3><input type="text" placeholder=""></h3>
		<h3><button class="buttons">Add text</button></h3>
      	<h3>Select image engraving</h3>
		<h3>
		<button class="design_select_buttons bike" title="Bikes" ></button>
		<button class="design_select_buttons church" title="Church"></button>
		<button class="design_select_buttons ice_cream" title="Ice Crean"></button>
		<button class="design_select_buttons nyc" title="New York City"></button>
		<button class="design_select_buttons space" title="Space"></button>
	  </h3>
		<h3><button class="buttons">Add to Cart</button></h3>
    </article>
  </section>
</div>	
</html>
