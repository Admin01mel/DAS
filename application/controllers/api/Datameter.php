<?php

require APPPATH . 'libraries/REST_Controller.php';

class Datameter extends REST_Controller
{

    /**
     * Get All Data from this method.
     *
     * @return Response
     */
    public function __construct()
    {
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
        if (!empty($id)) {
            $this->db->select('*');
            $this->db->from('das_power_mon');
            $this->db->where('id', $id);
            $data = $this->db->get()->result();
        } else {
            $this->db->select('*');
            $this->db->from('das_power_mon');
            $data = $this->db->get()->result();
        }

        $this->response($data, REST_Controller::HTTP_OK);
    }

    // /**
    //  * Get All Data from this method.
    //  *
    //  * @return Response
    //  */
    // public function index_post()
    // {
    //     $input = $this->input->post();
    //     $this->db->insert('daspower_config', $input);

    //     $this->response(['Item created successfully.'], REST_Controller::HTTP_OK);
    // }

    // /**
    //  * Get All Data from this method.
    //  *
    //  * @return Response
    //  */
    // public function index_put($id)
    // {
    //     $input = $this->put();
    //     $this->db->update('daspower_config', $input, array('id' => $id));

    //     $this->response(['Item updated successfully.'], REST_Controller::HTTP_OK);
    // }

    // /**
    //  * Get All Data from this method.
    //  *
    //  * @return Response
    //  */
    // public function index_delete($id)
    // {
    //     $this->db->delete('daspower_config', array('id' => $id));

    //     $this->response(['Item deleted successfully.'], REST_Controller::HTTP_OK);
    // }
}
