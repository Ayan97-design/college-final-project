<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
      integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr"
      crossorigin="anonymous"
    />
    <link
      href="https://fonts.googleapis.com/css?family=Dosis"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="css/main.css" />
    <title>Automobilioz| Home </title>
  </head>
  <body>
    <!-- Header -->
    <header id="header-home">
      <div class="container">
        <nav id="main-nav">
          <img src="img/logo.png" alt="Watch-logo" id="logo" />
          <ul>
            <li><a href="index.php" class="current">Home</a></li>
            <li><a href="about.php">About</a></li>
            <li><a href="Products.php">Products</a></li>
            <li><a href="contact.php">Contact</a></li>
            <li><a href="account.php">Account</a> <i class="fa fa-user" aria-hidden="true"></i></li>
            <li><a href="account.php">Cart</a>  <i class="fa fa-shopping-cart" aria-hidden="true"></i></li>
          </ul>
        </nav>
        <div class="header-content">
          <h1>
            Automobilioz
            <span
              class="txt-type"
              data-wait="3000"
              data-words='["Buy your", "favourite ", "Watch "]'
            ></span>
          </h1>
          <p  style=text-decoration: underline; class="lead">
          Our goal is to change the way you think about a Drive by delivering premium Rides at radically fair prices.
          </p>
          <a href="Products.php" class="btn-light">View Our Products</a>
        </div>
      </div>
    </header>

    

   <!-- Footer -->
   <?php
     include_once 'includes/footer.php';
?>

    <!-- Type Effect Tutorial: https://www.youtube.com/watch?v=POX3dT-pB4E -->
    <script src="js/typewriter.js"></script>
  </body>
</html>
