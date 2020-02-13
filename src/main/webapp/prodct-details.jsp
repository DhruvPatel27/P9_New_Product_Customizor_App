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
    <aside class="left_article"><img src="images/Mobile Covers/cherry-wood-phone.jpg" alt="" width="400" height="200" class="placeholder"/> </aside>
    <article class="right_article">
      <h3><strong>iPhone XR Case</strong></h3>
	  <h3><strong><h1>$25.00</h1></strong></h3>
      <p><ul>
			<li>Wood iPhone XR Case --Each case is unique with its own distinct wood grain,This protective phone case for iPhone XR combines dual layer Rubber and Real wood. Supports wireless charging
			</li>
			<li>ELEGANT & DURABLE: A perfect Stripes & stylish design that fits your iPhone XR perfectly while offers full protection (front, sides & back) with raised bezels that lift the screen and camera off flat surfaces
			</li>
			<li>Ergonomic design-Practical Protector, Thin, lightweight ,The iPhone XR Wood Case delivers effective protection against shocks, scratches, stains and dust
			</li>
		 </ul></p>
		
		<h3>Select Wood type</h3>
		<h3>
		<button class="wood_select_buttons cherry" title="Cherry" ></button>
		<button class="wood_select_buttons oak" title="Oak"></button>
		<button class="wood_select_buttons maple" title="Maple"></button>
		<button class="wood_select_buttons pine" title="Pine"></button>
		<button class="wood_select_buttons walnut" title="Walnut"></button>
        </h3>
		<h3>Enter personal message</h3>
		<h3><input class="personal_message" type="text" placeholder=""></h3>
		<h3><button class="buttons ">Add text</button><button class="buttons">Preview</button></h3>
      	<h3>Select image engraving</h3>
		<h3>
		<button class="design_select_buttons bike" title="Bikes" ></button>
		<button class="design_select_buttons church" title="Church"></button>
		<button class="design_select_buttons ice_cream" title="Ice Crean"></button>
		<button class="design_select_buttons nyc" title="New York City"></button>
		<button class="design_select_buttons space" title="Space"></button>
	  </h3>
		
		<h3><select class="quantity">
			<option value="0">Select quantity</option>
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			</select>
			<button class="buttons"><strong>Add to Cart</strong></button></h3>
    </article>
  </section>
</div>	
</html>
