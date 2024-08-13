<?php

if (!defined('BASEPATH'))
    exit('No direct script access allowed');

// Deklarasi pembuatan class Admin
class Beranda extends CI_Controller {
	
	// Konstrutor 
	function __construct() {
		parent::__construct();
		$this->load->model('Users_model');
		// if (!isset($this->session->userdata['username'])) {
		// 	redirect(base_url("login"));
		// }
	}
	
	// Fungsi untuk menampilkan halaman utama admin
	public function index() {
		// Menampilkan data berdasarkan id-nya yaitu username
		// $row = $this->Users_model->get_by_id($this->session->userdata['username']);
		// $data = array(	
		// 	'username' => $row->username,
		// 	'email'    => $row->email,
		// 	'level'    => $row->level,
		// );
		
		// $this->load->view('beranda',$data); // Menampilkan halaman utama admin
		$this->load->view('hmi');
		
	}
	
	// Fungsi melakukan logout
	function logout(){
		$this->session->sess_destroy();
		redirect(base_url('login'));
	}
}


?>