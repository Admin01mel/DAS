<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anouncer</title>
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/bootstrap.min.css')?>">
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/datatables/dataTables.bootstrap4.min.css')?>">
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/fontawesome-free-5.15.4-web/css/all.css')?>">
  <link rel="stylesheet" href="<?php echo base_url('assets/theme/css/jQKeyboard.css')?>">
  <style> body {
     background-color: #000000
 }

 .flex {
     -webkit-box-flex: 1;
     -ms-flex: 1 1 auto;
     flex: 1 1 auto
 }

 @media (max-width:991.98px) {
     .padding {
         padding: 1.5rem
     }
 }

 @media (max-width:767.98px) {
     .padding {
         padding: 1rem
     }
 }

 .padding {
     padding: 5rem

     
 }
 a{
     color: #f9f9fa;
 }

 
  </style>

</head>
<body>
 <div class="page-content page-container" id="page-content">
    <div class="padding">
        <div class="container d-flex justify-content-center">
            <div class="col-sm-12">
                <div class="mb-6">
                              <ul class="nav nav-pills" id="myTab" role="tablist">
                                 <li class="nav-item"><a class="nav-link active" id="home-tab" data-toggle="tab" href="#home2" role="tab" aria-controls="home" aria-selected="true">Device Setting</a></li>
                                 <li class="nav-item"><a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile2" role="tab" aria-controls="profile" aria-selected="false">Network Setting</a></li>
                                 <li class="nav-item"><a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact2" role="tab" aria-controls="contact" aria-selected="false">Display Setting</a></li>
                              </ul>
                           </div>
                           <div class="tab-content mb-6">
                              <div class="tab-pane fade show active" id="home2" role="tabpanel" aria-labelledby="home-tab">
                                 <div class="my-3 text-white " style="background-color:#000000;border-radius: 5px;">
                                       <div class="col-lg-12 " style="background-color:#1182bfb5 ;border-radius: 5px; padding : 5px 10px ">
                                        <h6>Device Setting</h6>
                                    </div>
                                    <div style="margin:10px;">
                                        <label class="jQKeyboard" for="code">Device Code</label>
                                        <input class="col-lg-12 form-control jQKeyboard key" type="text" name="" id="code" disabled>
                                        <div id="ip"></div>
                                    </div>
                                    <hr>
                                    <div style=" margin:10px">
                                        <label class="jQKeyboard" for="location">Location</label>
                                        <input class="col-lg-12 form-control jQKeyboard" type="text" name="" id="location">
                                    </div>
                                    <hr>
                                    <div style="margin:10px">
                                        <label class="jQKeyboard" for="name">Device Name</label>
                                        <input class="col-lg-12 form-control jQKeyboard" type="text" name="" id="name">
                                    </div>
                                    <hr>
                                    <div style="margin:10px">
                                        <label class="jQKeyboard" for="bot_name" >Bot Name</label>
                                        <input class="col-lg-12 form-control jQKeyboard" type="text" name="" id="bot_name" disabled>
                                    </div>
                                    <br>
                                    <div style="margin:10px">
                                        <button class="btn btn-danger font-weight-bold" id="btn-del" style="width:100%;"> <i
                                            class="fas fa-trash"></i> &nbsp
                                        Delete Log
                                        </button>
                                    </div>
                                    <div style="margin:10px">
                                        <button class="btn btn-primary font-weight-bold" id="btn-restart" style="width:100%;"> <i
                                            class="fa fa-refresh"></i> &nbsp
                                        Restart Device
                                        </button>
                                    </div>
                                     <button  style="margin:10px" class="btn btn-success flex-fill font-weight-bold" id="btnsave" style="height:40px;"><i class="fas fa-check-circle"></i>
                                        &nbsp
                                        SAVE
                                    </button>
                                    <hr>
                                </div>
                              </div>
                              <div class="tab-pane fade" id="profile2" role="tabpanel" aria-labelledby="profile-tab">
                                 <div class="my-3 text-white " style="background-color:#000000; border-radius: 5px;">
                                   <div class="col-lg-12 " style="background-color:#1182bfb5 ;border-radius: 5px; padding : 5px 10px ">
                                        <h6>Network Setting</h6>
                                    </div>
                                <div style="margin:10px;">
                                    <label class="jQKeyboard" for="ipserver">IP SERVER</label>
                                    <input class="col-lg-12 form-control jQKeyboard key" type="text" name="" id="ipserver">
                                    <div id="ip"></div>
                                </div>
                                <hr>
                                <div style=" margin:10px">
                                    <label class="jQKeyboard" for="ipaddress">IP ADDRESS</label>
                                    <input class="col-lg-12 form-control jQKeyboard" type="text" name="" id="ipaddress">
                                </div>
                                <hr>
                                <div style="margin:10px">
                                    <label class="jQKeyboard" for="netmask">NETMASK</label>
                                    <input class="col-lg-12 form-control jQKeyboard" type="text" name="" id="netmask">
                                </div>
                                <hr>
                                <div style="margin:10px">
                                    <label class="jQKeyboard" for="gateway">GATEWAY</label>
                                    <input class="col-lg-12 form-control jQKeyboard" type="text" name="" id="gateway">
                                </div>
                                <hr>
                                <div style="margin:10px">
                                    <label class="jQKeyboard" for="dns">DNS</label>
                                    <input class="col-lg-12 form-control jQKeyboard" type="text" name="" id="dns">
                                </div>
                                <hr>
                                <div class="d-flex justify-content-between flex-fill">
                                    <button class="btn btn-danger  flex-fill font-weight-bold" id="btncancel" style="height:40px;"> <i
                                            class="fas fa-chevron-circle-left"></i> &nbsp
                                        CANCEL
                                    </button>
                                    <button class="btn btn-success flex-fill font-weight-bold" id="btnsave" style="height:40px;"><i class="fas fa-check-circle"></i>
                                        &nbsp
                                        SAVE
                                    </button>
                                </div>
                            </div>
                              </div>
                              <div class="tab-pane fade" id="contact2" role="tabpanel" aria-labelledby="contact-tab">
                                 <!-- <form action="<?php echo $action; ?>" method="post"> -->
                                <div class="my-3 text-white " style="background-color:#000000 ;border-radius: 5px; ">
                                    <div class="col-lg-12 " style="background-color:#1182bfb5 ;border-radius: 5px; padding : 5px 10px ">
                                        <h6>Display Setting</h6>
                                    </div>
                                    <br>

                                    <div style="margin:10px; color:#00dcff">
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
                                      
                                         <div class="input-group-append">
                                               <input class="col-lg-12 form-control jQKeyboard" type="text" name="zoomW" id="zoomW" value="<?php echo $zoomW; ?>">
                                        </div>
                                    </div>
                                    <hr>
                                    <div style="margin:10px">
                                        <label class="jQKeyboard" for="Zoom Height" >Zoom Height</label>
                                        <input class="col-lg-12 form-control" type="text" name="zoomH" id="zoomH" value="<?php echo $zoomH;?>">
                                    </div>
                                    <hr>
                                    <!-- <div class="col-3" > -->
                                        <button style="margin:10px" class="btn btn-primary font-weight-bold"  id="btnsaveajah">
                                        Save Setting
                                        </button>
                                    <!-- </div> -->
                                    <hr>
                                </div>
                                <!-- </form> -->
                              </div>
                           </div>
                
            </div>
        </div>
    </div>
</div>

  <p hidden class="text-white" id="flg_set">home</p>
  <audio hidden controls id="alarm">
    <source src="assets/sound/audio.wav" type="audio/wav">
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

    <a id="btn-home" class="flex-fill btn  text-center text-success" onclick="window.location.href='./beranda'">
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

    <a class="flex-fill btn text-center text-secondary" onclick="window.location.href='config'"  id="nav-config">
      <i class="fas fa-cog icon-nav" aria-hidden="true"></i>
      <br>CONFIG DISPLAY</a>


    <!-- <a class="flex-fill btn text-center text-secondary" onclick="gotolog()" id="nav-log">
      <i class="fas fa-address-book icon-nav" aria-hidden="true"></i>
      <br>LOG</a> -->


    <a class="flex-fill btn text-center text-secondary" onclick="activate(document.documentElement);" id="nav-exp">
      <i class="fas fa-expand icon-nav" aria-hidden="true"></i>
      <br>EXPAND</a>

    </ul>

  </div>
 

 <script src="<?php echo base_url('assets/theme/js/jquery.min.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/bootstrap.min.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/jQKeyboard.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/sweetalert2.all.min.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/DataTables/dataTables.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/jspdf.min.js')?>"></script>
  <script src="<?php echo base_url('assets/theme/js/jspdf.plugin.autotable.min.js')?>"></script>

  <script>
    //first load
   
    $.ajax({
        method: "get",
        url: 'backend/webapi/viewsetting.php'
    }).done(function (msg) {
        let data = JSON.parse(msg)
        $('#code').val(data[0].kode_mesin)
        $('#bot_name').val(data[0].botname)
        $('#location').val(data[0].lokasi)
        $('#name').val(data[0].nama)

        $('#ipserver').val(data[0].ipserver)
        $('#ipaddress').val(data[0].iplocal)
        $('#netmask').val(data[0].netmask)
        $('#gateway').val(data[0].gateway)
        $('#dns').val(data[0].dns)
    })

    //keyboard service
    $('#ipserver').click(function () {

        $('#key').show()
        $('#key').removeClass('pos2')
        $('#key').removeClass('pos3')
        $('#key').removeClass('pos4')
        $('#key').removeClass('pos5')
        $('#key').addClass('pos1')
    })
    $('#ipaddress').click(function () {
        $('#key').show()
        $('#key').removeClass('pos1')
        $('#key').removeClass('pos3')
        $('#key').removeClass('pos4')
        $('#key').removeClass('pos5')
        $('#key').addClass('pos2')
    })
    $('#netmask').click(function () {
        $('#key').show()
        $('#key').removeClass('pos1')
        $('#key').removeClass('pos2')
        $('#key').removeClass('pos4')
        $('#key').removeClass('pos5')
        $('#key').addClass('pos3')
    })
    $('#gateway').click(function () {
        $('#key').show()
        $('#key').removeClass('pos1')
        $('#key').removeClass('pos2')
        $('#key').removeClass('pos3')
        $('#key').removeClass('pos5')
        $('#key').addClass('pos4')
    })
    $('#dns').click(function () {
        $('#key').show()
        $('#key').removeClass('pos1')
        $('#key').removeClass('pos2')
        $('#key').removeClass('pos3')
        $('#key').removeClass('pos4')
        $('#key').addClass('pos5')
    })

    var keyboard = {
        'layout': [
            // alphanumeric keyboard type
            // text displayed on keyboard button, keyboard value, keycode, column span, new row
            [
                [
                    ['`', '`', 192, 0, true], ['1', '1', 49, 0, false], ['2', '2', 50, 0, false], ['3', '3', 51, 0, false], ['4', '4', 52, 0, false], ['5', '5', 53, 0, false], ['6', '6', 54, 0, false],
                    ['7', '7', 55, 0, false], ['8', '8', 56, 0, false], ['9', '9', 57, 0, false], ['0', '0', 48, 0, false], ['-', '-', 189, 0, false], ['=', '=', 187, 0, false],
                    ['q', 'q', 81, 0, true], ['w', 'w', 87, 0, false], ['e', 'e', 69, 0, false], ['r', 'r', 82, 0, false], ['t', 't', 84, 0, false], ['y', 'y', 89, 0, false], ['u', 'u', 85, 0, false],
                    ['i', 'i', 73, 0, false], ['o', 'o', 79, 0, false], ['p', 'p', 80, 0, false], ['[', '[', 219, 0, false], [']', ']', 221, 0, false], ['&#92;', '\\', 220, 0, false],
                    ['a', 'a', 65, 0, true], ['s', 's', 83, 0, false], ['d', 'd', 68, 0, false], ['f', 'f', 70, 0, false], ['g', 'g', 71, 0, false], ['h', 'h', 72, 0, false], ['j', 'j', 74, 0, false],
                    ['k', 'k', 75, 0, false], ['l', 'l', 76, 0, false], [';', ';', 186, 0, false], ['&#39;', '\'', 222, 0, false], ['Enter', '13', 13, 3, false],
                    ['Shift', '16', 16, 2, true], ['z', 'z', 90, 0, false], ['x', 'x', 88, 0, false], ['c', 'c', 67, 0, false], ['v', 'v', 86, 0, false], ['b', 'b', 66, 0, false], ['n', 'n', 78, 0, false],
                    ['m', 'm', 77, 0, false], [',', ',', 188, 0, false], ['.', '.', 190, 0, false], ['/', '/', 191, 0, false], ['Shift', '16', 16, 2, false],
                    ['Bksp', '8', 8, 3, true], ['Space', '32', 32, 12, false], ['Clear', '46', 46, 3, false], ['Cancel', '27', 27, 3, false]
                ]
            ]
        ]
    }
    $('input.jQKeyboard').initKeypad({ 'keyboardLayout': keyboard });

    $('#btn-del').click(function () {
        $("#valmodal").modal('show')
        $("#text-config").text("Do you want to delete data?")
        $("#conf-text").text("del")
    });
    $('#btn-restart').click(function () {
        $("#valmodal").modal('show')
        $("#text-config").text("Do you want to Restart device?")
        $("#conf-text").text("rest")
    });
    $('#btn-yes').click(function () {
        let conf =   $("#conf-text").text()
       if(conf =="del"){
           deletedevice();
       }
       else if(conf=="rest"){
          restartdevice()
       }
    });
    $('#btn-no').click(function(){
        $("#valmodal").modal('hide')
    })
    function deletedevice(){
        $.ajax({
            method:"get",
            url: 'backend/webapi/deletelog.php'
        }).done(function(){Swal.fire({
                    position: 'top-center',
                    icon: 'success',
                    title: 'Your data has been deleted',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function () {  $("#valmodal").modal('hide') })
           
        })
    }
    function restartdevice(){
        $.ajax({
            method:"get",
            url: 'backend/webapi/reboot.php'
        }).done(function(){Swal.fire({
                    position: 'top-center',
                    icon: 'success',
                    title: 'device is restarted',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function () {  $("#valmodal").modal('hide') })
           
        })
    }
    $('#btncancel').click(function () {
        gotohome()
    });
    $('#btnsaveajah').click(function () {
        let port = $('#port').val();
        let zoomW = $('#zoomW').val();
        let zoomH = $('#zoomH').val();
        $.ajax({
            method: "post",
            // headers: {'Content-Type': 'application/json'}, 
            // body: JSON.stringify(data),
            url: 'api/params/admin',
            data: {
                total_port: port,
                zoom_w: zoomW,
                zoom_h: zoomH,

            }
        }).done(function (msg) {

             let data = (msg)
            if(data.code==1){
                Swal.fire({
                    position: 'top-center',
                    icon: 'success',
                    title: 'Your data has been saved',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function () { gotohome() })
             }
             else{
                 alert(msg)
             }
            // alert('update success')
        })
    });

     $('#btnsave').click(function () {
        let ipserver = $('#ipserver').val();
        let ipaddress = $('#ipaddress').val();
        let netmask = $('#netmask').val();
        let gateway = $('#gateway').val();
        let dns = $('#dns').val();
        let name = $('#name').val();
        let loc = $('#location').val();
        $.ajax({
            method: "post",
            url: 'backend/webapi/updatesetting.php',
            data: {
                ipserver: ipserver,
                ipaddr: ipaddress,
                netmask: netmask,
                gateway: gateway,
                dns: dns,
                loc:loc,
                name:name,

            }
        }).done(function (msg) {

             let data = JSON.parse(msg)
            if(data.code==1){
                Swal.fire({
                    position: 'top-center',
                    icon: 'success',
                    title: 'Your data has been saved',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function () { gotohome() })
             }
             else{
                 alert(msg)
             }
            // alert('update success')
        })
    });


</script>

  <script>
    var width = window.innerWidth
    if(width<600)
    {
      $("#nav-exp").addClass("hide")
    }
    $(document).ready(function () {
      //document.addEventListener('contextmenu', event => event.preventDefault());
      $("#main").load("main/home.php?p=<?php echo $port ?>");
      readmute();
      
    });
    function showauth(){
      $("#bd-auth").load("main/auth.html")
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

      $("#main").load("main/setting.html");
    }
    function gotohome() {
      $("#flg_set").text("home")
      $("#nav-log").removeClass("text-success")
      $("#nav-config").removeClass("text-success")
      $("#btn-home").removeClass("text-secondary")
      $("#btn-home").addClass("text-success")
      $("#main").load("main/home.php?p=<?php echo $port ?>");
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
      $("#main").load("main/log.html");
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
        url: "backend/webapi/resetflag.php"
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
        url: "backend/webapi/readmute.php"
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
        url: "backend/webapi/readmute.php?w=" + data
      }).done(function (msg) {
        console.log(msg)
      })
    }
    function updack(data) {
      $.ajax({
        method: "get",
        url: "backend/webapi/readack.php?w=" + data
      }).done(function (msg) {
        console.log(msg)
      })
    }
    function updrst(data) {
      $.ajax({
        method: "get",
        url: "backend/webapi/readreset.php?w=" + data
      }).done(function (msg) {
        console.log(msg)
      })
    }

    const loopalarm = setInterval(readalarm, 1000);
    function readalarm() {
      $.ajax({
        method: "get",
        url: "backend/webapi/countalarm.php"
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