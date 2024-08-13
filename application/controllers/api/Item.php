<?php
   
require APPPATH . 'libraries/REST_Controller.php';
     
class Item extends REST_Controller {
    
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
    public function index_post()
    {
        $input = $this->input->post();
        $this->db->insert('items',$input);
     
        $this->response(['Item created successfully.'], REST_Controller::HTTP_OK);
    } 
     
    /**
     * Get All Data from this method.
     *
     * @return Response
    */
    public function index_put($id)
    {
        $input = $this->put();
        $this->db->update('items', $input, array('id'=>$id));
     
        $this->response(['Item updated successfully.'], REST_Controller::HTTP_OK);
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