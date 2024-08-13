<?php
	ini_set('display_errors', '0');
    ini_set('error_reporting', E_ALL);
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anouncer</title>
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/bootstrap.min.css')?>">
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/datatables/dataTables.bootstrap4.min.css')?>">

  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/maindas.css')?>">
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/fontawesome-free-5.15.4-web/css/all.css')?>">
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/jQKeyboard.css')?>">





</head>
<style>
  .icon-nav {
    font-size: 25px;
    text-align: center;
  }

  .a:hover {
    background-color: greenyellow;
  }

  .kotak {
	/* width: 210px;
	height: 60px; */
    width: calc(200*<?php echo $zoomW;?>px);
	height: calc(76*<?php echo $zoomH;?>px);
	padding-top: 1px;
	margin-top: 10px;
	border-radius: 10px;
	/* border: 1px solid white; */
}

  .title {
    background-color: black;
    margin-top: 0px;
    height: 30px;
    padding: 2px 0;
  }
  @media only screen and (max-width: 1281px) {
	/* For tablets: */

	.kotak {
		font-size: 17px;
		width: calc(200*<?php echo $zoomW;?>px);
		height: calc(76*<?php echo $zoomH;?>px);
		padding-top: 12px;
		margin-top: 10px;
		border-radius: 5px;
	}

	.btn-menu {
		height: 50px;
		width: 95%;
		text-align: center;
		vertical-align: middle;
		background: conic-gradient(
			#d7d7d7,
			#c3c3c3,
			#cccccc,
			#c6c6c6,
			#d7d7d7,
			#c3c3c3,
			#cccccc,
			#c6c6c6,
			#d7d7d7,
			#c3c3c3,
			#cccccc,
			#c6c6c6,
			#d7d7d7,
			#c3c3c3,
			#cccccc,
			#c6c6c6
		);
	}

	.btn-dot {
		height: 50px;
		width: 110px;
		border-radius: 10%;
		display: inline-block;
		margin: 3px;
		text-align: center;
		vertical-align: middle;
		background: conic-gradient(
			#d7d7d7,
			#c3c3c3,
			#cccccc,
			#c6c6c6,
			#d7d7d7,
			#c3c3c3,
			#cccccc,
			#c6c6c6,
			#d7d7d7,
			#c3c3c3,
			#cccccc,
			#c6c6c6,
			#d7d7d7,
			#c3c3c3,
			#cccccc,
			#c6c6c6
		);
	}
}

</style>

<body style="background-color:#1c222c">

  
 <!-- <div style="margin-top:15px" id="main" class="col-lg-12">

  </div> -->
<form action="<?php echo $action; ?>" method="post">
  <div class="my-3 bg-dark text-white " style="border-radius: 5px; ">
    <div class="bg-success col-lg-12 " style="border-radius: 5px; padding : 5px 10px ">
        <h5>View Setting</h5>
    </div>
    <br>

    <div style="margin:10px; color:orange;">
        <p>This setting only affects the user, not on the screen installed on the panel.</p>
    </div>
    <div style="margin:10px;">
        <label class="jQKeyboard" for="code">Displayed Port</label>
        <input class="col-lg-12 form-control jQKeyboard key" type="number" name="port" id="port" value="<?php echo $port;  ?>">
        <div id="ip"></div>
    </div>
    <hr>
    <div style="margin:10px">
        <label class="jQKeyboard" for="Zoom Width">Zoom Width</label>
        <input class="col-lg-12 form-control jQKeyboard" type="text" name="zoomW" id="zoomW" value="<?php echo $zoomW."x"; ?>">
    </div>
    <hr>
    <div style="margin:10px">
        <label class="jQKeyboard" for="Zoom Height" >Zoom Height</label>
        <input class="col-lg-12 form-control" type="text" name="zoomH" id="zoomH" value="<?php echo $zoomH."x"; ?>">
    </div>
    <br>
    <div style="margin:10px">
        <button class="btn btn-primary font-weight-bold" type="submit" id="btn-restart" style="width:100%;">
        Save Setting
        </button>
    </div>
    <hr>
</div>
</form>
  <p hidden class="text-white" id="flg_set">home</p>
  <audio hidden controls id="alarm">
    <source src="../assets/sound/audio.wav" type="audio/wav">
  </audio>
  <div hidden id="key" style="z-index:2 ;
  left: 0%;right:0%; display: flex;
    justify-content: space-around;
    scale:2.5">
  </div>
  <p hidden id="port">0</p>
  <p hidden id="mute-config">0</p>
  <p hidden class="text-success" id="ack-config">0</p>
  <div class="fixed-bottom d-flex justify-content-between align-content-md-stretch bg-dark"
    style="padding-top:1px;padding-bottom:1px;">

    <a id="btn-home" class="flex-fill btn  text-center text-success" onclick="window.location.href='../beranda'">
      <i class="fas fa-home icon-nav" aria-hidden="true">&nbsp</i><br>
      HOME</a>

    <a id="btn-mute" class="flex-fill  btn text-center text-secondary" onclick="muteaudio()">
      <i class="fas fa-volume-up  icon-nav" aria-hidden="true" id="audio"></i><br>
      MUTE</a>

    <a id="btn-ack" class="flex-fill btn text-center text-secondary" onclick="ack()">
      <i class="fas fa-stop icon-nav" aria-hidden="true"></i>
      <br>ACK</a>


    <a class=" flex-fill btn text-center text-secondary" onclick="reset()">
      <i class="fa fa-sync-alt icon-nav" aria-hidden="true"></i>
      <br>RESET</a>

    <a class="flex-fill btn text-center text-secondary" onclick="gotosetting()" id="nav-config">
      <i class="fas fa-cog icon-nav" aria-hidden="true"></i>
      <br>CONFIG DISPLAY</a>


    <a class="flex-fill btn text-center text-secondary" onclick="gotolog()" id="nav-log">
      <i class="fas fa-address-book icon-nav" aria-hidden="true"></i>
      <br>LOG</a>


    <a class="flex-fill btn text-center text-secondary" onclick="activate(document.documentElement);" id="nav-exp">
      <i class="fas fa-expand icon-nav" aria-hidden="true"></i>
      <br>EXPAND</a>

    </ul>

  </div>
 


  <div class="modal fade " id="authmodal" tabindex="-1" role="dialog" aria-labelledby="authmodal" aria-hidden="true" >
    <div class="modal-dialog" role="document">
      <div class="modal-content bg-dark col-md-10" style="border-radius: 10px;">
        <div class="modal-body " id="bd-auth" style="border: 10px;">
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade " id="valmodal" tabindex="-1" role="dialog" aria-labelledby="authmodal" aria-hidden="true" >
    <div class="modal-dialog" role="document">
      <div class="modal-content bg-dark col-md-10" style="border-radius: 10px;">
        <div class="modal-body " id="bd-val" style="border: 10px;">
          <p hidden id="conf-text"></p>
          <h5 id="text-config" class="text-white"></h5>
          <hr>

          <div style="  margin-right:10px;" class="col-md-12 text-right">

          <button class="col-md-3 btn btn-danger" id="btn-yes">Yes</button>
          <button class="col-md-3 btn btn-secondary" id="btn-no">No</button>
          </div>
        </div>
      </div>
    </div>
  </div>


  <script src="<?php echo base_url('assets/theme/js/jquery.min.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/bootstrap.min.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/jQKeyboard.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/sweetalert2.all.min.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/DataTables/dataTables.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/jspdf.min.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/jspdf.plugin.autotable.min.js')?>"></script>



  <script>
    var width = window.innerWidth
    if(width<600)
    {
      $("#nav-exp").addClass("hide")
    }
    $(document).ready(function () {
      //document.addEventListener('contextmenu', event => event.preventDefault());
      $("#main").load("../main/home.php");
      readmute();
      
    });
    function showauth(){
      $("#bd-auth").load("../main/auth.html")
     $("#authmodal").modal('show');
    }
    // function gotoconfig() {
    //   $("#flg_set").text("net")
    //   $("#nav-log").removeClass("text-success")
    //   $("#btn-home").removeClass("text-success")
    //   $("#nav-log").addClass("text-secondary")
    //   $("#btn-home").addClass("text-secondary")
    //   $("#nav-config").addClass("text-success")
    //   stoploop()
    //   showauth()    
    //   $("#key").hide()
    // }
    function gotosetting() {
      $("#key").hide()
      stoploop()

      $("#main").load("../main/setting.html");
    }
    function gotohome() {
      $("#flg_set").text("home")
      $("#nav-log").removeClass("text-success")
      $("#nav-config").removeClass("text-success")
      $("#btn-home").removeClass("text-secondary")
      $("#btn-home").addClass("text-success")
      $("#main").load("../main/home.php");
      $("#key").hide()
    }
    function gotolog() {
      stoploop()
      $("#key").hide()
      $("#nav-config").addClass("text-secondary")
      $("#nav-config").removeClass("text-success")
      $("#btn-home").addClass("text-secondary")
      $("#btn-home").removeClass("text-success")
      $("#nav-log").addClass("text-success")
      $("#main").load("../main/log.html");
    }
    function muteaudio() {

      if ($('#mute-config').text() == 0) {
        $('#alarm').prop("muted", true);
        $('#mute-config').text(1)
        $('#btn-mute').removeClass('text-secondary')
        $('#btn-mute').addClass('text-danger')
        $('#audio').removeClass('fa-volume-up')
        $('#audio').addClass('fa-volume-mute')
        updmute(1)
      }
      else {
        $('#btn-mute').removeClass('text-danger')
        $('#btn-mute').addClass('text-secondary')
        $('#alarm').prop("muted", false);
        $('#mute-config').text(0)
        $('#audio').removeClass('fa-volume-mute')
        $('#audio').addClass('fa-volume-up')
        updmute(0)
      }
    }
    function ack() {

      $('#alarm').prop("muted", true);
      $('#mute-config').text(1)
      $('#btn-mute').removeClass('text-secondary')
      $('#btn-mute').addClass('text-danger')
      $('#audio').removeClass('fa-volume-up')
      $('#audio').addClass('fa-volume-mute')
      $('#ack-config').text(1)
      $('#btn-ack').removeClass('text-secondary')
      $('#btn-ack').addClass('text-warning')
      $("#btn-mute").attr("disabled", true);
      updmute(1)
      updack(1)
    }
    function reset() {
      $.ajax({
        method: "get",
        url: "../backend/webapi/resetflag.php"
      }).done(function (msg) {
        $('#ack-config').text(0)
        $('#alarm').prop("muted", false);
        $('#mute-config').text(0)
        $('#btn-mute').removeClass('text-danger')
        $('#btn-mute').addClass('text-secondary')
        $('#audio').removeClass('fa-volume-mute')
        $('#audio').addClass('fa-volume-up')
        $('#btn-ack').removeClass('text-warning')
        $('#btn-ack').addClass('text-secondary')
        updmute(0);
        updack(0)
        updrst(1)
      })

    }


    if (window.history.replaceState) {
      window.history.replaceState(null, null, window.location.href);
    }
    function readmute() {
      $.ajax({
        methode: "get",
        url: "../backend/webapi/readmute.php"
      }).done(function (msg) {
        if (msg == "1") {
          $('#alarm').prop("muted", true);
          $('#mute-config').text(1)
          $('#btn-mute').removeClass('text-secondary')
          $('#btn-mute').addClass('text-danger')
          $('#audio').removeClass('fa-volume-up')
          $('#audio').addClass('fa-volume-mute')
        }
        else if (msg == "0") {
          $('#btn-mute').removeClass('text-danger')
          $('#btn-mute').addClass('text-secondary')
          $('#alarm').prop("muted", false);
          $('#mute-config').text(0)
          $('#audio').removeClass('fa-volume-mute')
          $('#audio').addClass('fa-volume-up')
        }
      })

    }
    function updmute(data) {
      $.ajax({
        method: "get",
        url: "../backend/webapi/readmute.php?w=" + data
      }).done(function (msg) {
        console.log(msg)
      })
    }
    function updack(data) {
      $.ajax({
        method: "get",
        url: "../backend/webapi/readack.php?w=" + data
      }).done(function (msg) {
        console.log(msg)
      })
    }
    function updrst(data) {
      $.ajax({
        method: "get",
        url: "../backend/webapi/readreset.php?w=" + data
      }).done(function (msg) {
        console.log(msg)
      })
    }

    const loopalarm = setInterval(readalarm, 1000);
    function readalarm() {
      $.ajax({
        method: "get",
        url: "../backend/webapi/countalarm.php"
      }).done(function (msg) {
        let data = JSON.parse(msg)
        let jml = data[0].jml
        // alert(document.getElementById('alarm').play())
        if (jml > 0) {
          document.getElementById('alarm').play();
        }
        else {
          document.getElementById('alarm').pause();
        }
      })
      readmute()
      //alert('h')
    }

    function activate(ele) {
      if (ele.requestFullscreen) {
        ele.requestFullscreen();
        document.getElementById(full).style.display = "hidden";
      }
    }
    function getdate(){
    return  new Date().toLocaleString().replace(",","").replace(/:.. /," ");
    }

  </script>

</body>

</html>