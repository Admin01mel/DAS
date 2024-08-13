<?php

if (!defined('BASEPATH'))
	exit('No direct script access allowed');

// Deklarasi pembuatan class Admin
class Users extends CI_Controller
{

	// Konstrutor 
	function __construct()
	{
		parent::__construct();
		$this->load->model('Users_model');
		$this->load->model('View_model');
		$this->load->library('datatables');
		if (!isset($this->session->userdata['username'])) {
			redirect(base_url("login"));
		}
	}

	public function json()
	{
		header('Content-Type: application/json');
		echo $this->Users_model->json();
	}


	// Fungsi untuk menampilkan halaman utama admin
	// public function index()
	// {
	// 	// Menampilkan data berdasarkan id-nya yaitu username
	// 	$row = $this->View_model->get_by_id($this->session->userdata['username']);
	// 	$rowlevel = $this->Users_model->get_by_id($this->session->userdata['username']);
	// 	$data = array(
	// 		'username' => $row->username,
	// 		'level'    => $rowlevel->level,
	// 		'port'     => $row->total_port,
	// 		'zoomW'    => $row->zoom_w,
	// 		'zoomH'    => $row->zoom_h,

	// 	);

	// 	// $this->load->view('beranda',$data); // Menampilkan halaman utama admin
	// 	$this->load->view('beranda', $data);
	// }
	 public function delete($id){
		// Jika session data username tidak ada maka akan dialihkan kehalaman login			
		if (!isset($this->session->userdata['username'])) {
			redirect(base_url("login"));
		}
	
        $row = $this->Users_model->get_by_id($id);
		
		//jika id users yang dipilih tersedia maka akan dihapus
        if ($row) {
            $this->Users_model->delete($id);
            $this->session->set_flashdata('message', 'Delete Record Success');
            redirect(site_url('beranda'));
        } 
		//jika id users yang dipilih tidak tersedia maka akan muncul pesan 'Record Not Found'
		else {
            $this->session->set_flashdata('message', 'Record Not Found');
            redirect(site_url('beranda'));
        }
    }

	// Fungsi melakukan logout
	function logout()
	{
		$this->session->sess_destroy();
		redirect(base_url('login'));
	}
}
