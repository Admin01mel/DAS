<?php

if (!defined('BASEPATH'))
	exit('No direct script access allowed');

// Deklarasi pembuatan class Admin
class Beranda extends CI_Controller
{

	// Konstrutor 
	function __construct()
	{
		parent::__construct();
		$this->load->model('Users_model');
		$this->load->model('View_model');
		if (!isset($this->session->userdata['username'])) {
			redirect(base_url("login"));
		}
	}

	// Fungsi untuk menampilkan halaman utama admin
	public function index()
	{
		// Menampilkan data berdasarkan id-nya yaitu username
		$row = $this->View_model->get_by_id($this->session->userdata['username']);
		$rowlevel = $this->Users_model->get_by_id($this->session->userdata['username']);
		$data = array(
			'username' => $row->username,
			'level'    => $rowlevel->level,
			'port'     => $row->total_port,
			'zoomW'    => $row->zoom_w,
			'zoomH'    => $row->zoom_h,
			'fontSize' => $row->font_size,

		);

		// $this->load->view('beranda',$data); // Menampilkan halaman utama admin
		$this->load->view('beranda', $data);
	}

	// Fungsi melakukan logout
	function logout()
	{
		$this->session->sess_destroy();
		redirect(base_url('login'));
	}
}
