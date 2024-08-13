<?php

if (!defined('BASEPATH'))
    exit('No direct script access allowed');

// Deklarasi pembuatan class Admin
class Device extends CI_Controller {
	
	// Konstrutor 
	function __construct() {
		parent::__construct();
		$this->load->model('Device_model');
	}
	
	public function index() {
		$this->load->view('login');
		
	}

	public function das33d832bbe563279ba4854ec3beef345bdf() {
		$row = $this->Device_model->get_all();
		$data = array(	
			'zoomW'    => $row->zoom_w,
			'zoomH'    => $row->zoom_h,
			'fontSize' => $row->f_size
		);
		
		$this->load->view('beranda2',$data);
		
	}

}


?>