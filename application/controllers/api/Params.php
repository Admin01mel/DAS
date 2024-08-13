<?php
   
require APPPATH . 'libraries/REST_Controller.php';
     
class Params extends REST_Controller {
    
	  /**
     * Get All Data from this method.
     *
     * @return Response
    */
    public function __construct() {
       parent::__construct();
       $this->load->database();
    }
       
    /**
     * Get All Data from this method.
     *
     * @return Response
    */
	public function index_get($id = 0)
	{
        if(!empty($id)){
             $this->db->select('mesin.*,m_mesin.kode_gi as nama_gi,m_mesin.nama');
            $this->db->from('mesin');
            $this->db->join('m_mesin','m_mesin.kode_mesin = mesin.kode_mesin');
            $this->db->limit($id);
            $data = $this->db->get()->result();
        }else{
            $this->db->select('*');
            $this->db->from('mesin');
            $this->db->join('m_mesin','m_mesin.kode_mesin = mesin.kode_mesin');
            $this->db->order_by('mesin.port', 'ASC');
            $data = $this->db->get()->result();
        }
     
        $this->response($data, REST_Controller::HTTP_OK);
	}
      
    /**
     * Get All Data from this method.
     *
     * @return Response
    */
    public function index_post($id)
    {
        $input = $this->input->post();
        $this->db->update('view_setting', $input, array('username'=>$id));
           $message = array(
            'code' => 1,
        );
     
        $this->response($message);
    } 
     
    /**
     * Get All Data from this method.
     *
     * @return Response
    */
    public function index_put($id)
    {
        $input = $this->put();
        $this->db->update('view_setting', $input, array('id'=>$id));
     
        $this->response(['params updated successfully.'], REST_Controller::HTTP_OK);
    }
     
    /**
     * Get All Data from this method.
     *
     * @return Response
    */
    public function index_delete($id)
    {
        $this->db->delete('items', array('id'=>$id));
       
        $this->response(['Item deleted successfully.'], REST_Controller::HTTP_OK);
    }
    	
}