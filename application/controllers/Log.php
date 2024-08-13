<?php

if (!defined('BASEPATH'))
    exit('No direct script access allowed');

// Deklarasi pembuatan class Admin
class Log extends CI_Controller {
	
	// Konstrutor 
	function __construct() {
		parent::__construct();
		$this->load->model('Users_model');
		$this->load->model('View_model');
		if (!isset($this->session->userdata['username'])) {
			redirect(base_url("login"));
		}
	}
	
	// Fungsi untuk menampilkan halaman utama admin
	public function index() {
		// Menampilkan data berdasarkan id-nya yaitu username
		$row = $this->View_model->get_by_id($this->session->userdata['username']);
		$data = array(
			'action'   => site_url('setting/save_action'),	
			'username' => $row->username,
			'port'    => $row->total_port,
			'zoomW'    => $row->zoom_w,
			'zoomH'    => $row->zoom_h,
			
		);
		
		// $this->load->view('beranda',$data); // Menampilkan halaman utama admin
		$this->load->view('log',$data);
		
	}

	public function save_action(){
		
	// Jika session data username tidak ada maka akan dialihkan kehalaman login			
	if (!isset($this->session->userdata['username'])) {
		redirect(base_url("login"));
	
	
	}

	$rowAdm = $this->Users_model->get_by_id($this->session->userdata['username']);
	$id=$rowAdm->username;
	$row = $this->View_model->get_by_id($id);


	$displayedPort = $this->input->post('port',TRUE);
	$zoomWidth = $this->input->post('zoomW',TRUE);
	$zoomHeight = $this->input->post('zoomH',TRUE);


	if ($row) {
		$simpan = array(
			'total_port' => $displayedPort,
			'zoom_w' 	 => substr($zoomWidth,0,-1),
			'zoom_h'  	 => substr($zoomHeight,0,-1),
		);
	}
	   $this->View_model->update($id, $simpan);
	// $this->Tanaman_model->update($this->input->post($id, $simpan));
	redirect(site_url('setting'));	
	
			
	}	
	
	// Fungsi melakukan logout
	function logout(){
		$this->session->sess_destroy();
		redirect(base_url('login'));
	}
}


?>