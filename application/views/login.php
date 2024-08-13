<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Digital Alert System</title>

  <!-- Google Font: Source Sans Pro -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/adminlte/plugins/fontawesome-free/css/all.min.css')?>">

  <!-- icheck bootstrap -->
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/adminlte/plugins/icheck-bootstrap/icheck-bootstrap.min.css')?>">
 
  <!-- Theme style -->
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/adminlte/dist/css/adminlte.min.css')?>">
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/animateBackground.css')?>">

  
</head>
<div ></div>
<body class="hold-transition login-page">
<canvas></canvas>
<div class="login-box">
  <!-- /.login-logo -->
  <div class="card card-outline card-primary">
    <div class="text-center">
      <br>
      <img src="<?php echo base_url('assets/pic/pln-logo.png')?>" width="175px" alt="">
      <br>
      <br>

    </div>
    <div class="card-header text-center">
      <a href="#" class="h5"><b>Digital Alert System</b></a>
      <br>
      <small><em>Realtime for your reporting system</em></small>
    </div>
    <div class="card-body">
      <!-- <p class="login-box-msg">Sign in to start your session</p> -->

      <form action="<?php echo base_url('login/proses')?>" method="post">
        <div class="input-group mb-3">
          <input name="username" type="text" class="form-control" placeholder="Username">
          <div class="input-group-append">
            <div class="input-group-text">
              <span class="fas fa-user"></span>
            </div>
          </div>
        </div>
        <div class="input-group mb-3">
          <input name="password" type="password" class="form-control" placeholder="Password">
          <div class="input-group-append">
            <div class="input-group-text">
              <span class="fas fa-lock"></span>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-8">
           
          </div>
          <!-- /.col -->
          <div class="col-4">
            <button type="submit" class="btn btn-primary btn-block">Sign In</button>
          </div>
          <!-- /.col -->
        </div>
      </form>

  
      <!-- /.social-auth-links -->

   
    </div>
    <!-- /.card-body -->
  </div>
  <!-- /.card -->
</div>

<!-- /.login-box -->

<!-- jQuery -->
<!-- <script src="../../plugins/jquery/jquery.min.js"></script> -->
<script src="<?php echo base_url('assets/theme/adminlte/plugins/jquery/jquery.min.js')?>"></script>

<!-- Bootstrap 4 -->
<script src="<?php echo base_url('assets/theme/adminlte/plugins/bootstrap/js/bootstrap.bundle.min.js')?>"></script>

<!-- AdminLTE App -->
<script src="<?php echo base_url('assets/theme/adminlte/dist/js/adminlte.min.js')?>"></script>
<script src="<?php echo base_url('assets/theme/js/animateBackground.js')?>"></script>
</body>
</html>
