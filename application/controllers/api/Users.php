<?php

require APPPATH . 'libraries/REST_Controller.php';

class Users extends REST_Controller
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
            $this->db->from('users');
            $this->db->where('username', $id);
            $data = $this->db->get()->result();
        } else {
            $this->db->select('*');
            $this->db->from('users');
            $data = $this->db->get()->result();
        }

        $this->response($data, REST_Controller::HTTP_OK);
    }

    /**
     * Get All Data from this method.
     *
     * @return Response
     */
    public function index_post($id = 0)
    {

        if (!empty($id)) {
        $input = $this->input->post();
        $input['id_session'] = md5($input['password']);
        $input['password'] = md5($input['password']);
        $viewinput['username'] = $input['username'];
        $this->db->update('users', $input, array('username' => $id));
        $this->db->update('view_setting', $viewinput, array('username' => $id));
        $message = array('code' => 1,);
        $this->response($message);
        } else{
        $input = $this->input->post();
        $input['id_session'] = md5($input['password']);
        $input['password'] = md5($input['password']);
        $viewinput['username'] = $input['username'];
        $viewinput['total_port'] = '48';
        $viewinput['zoom_w'] = '1';
        $viewinput['zoom_h'] = '1';
        $viewinput['font_size'] = '12';
        $this->db->insert('users',$input);
        $this->db->insert('view_setting',$viewinput);
        $message = array('code' => 1, );
        $this->response($message);
        }


        
    }

    /**
     * Get All Data from this method.
     *
     * @return Response
     */
    public function index_put($id)
    {
        $input = $this->put();
        $this->db->update('items', $input, array('id' => $id));

        $this->response(['Item updated successfully.'], REST_Controller::HTTP_OK);
    }

    /**
     * Get All Data from this method.
     *
     * @return Response
     */
    public function index_delete($id)
    {
        $this->db->delete('items', array('id' => $id));

        $this->response(['Item deleted successfully.'], REST_Controller::HTTP_OK);
    }
}
