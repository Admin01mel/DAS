<?php

require APPPATH . 'libraries/REST_Controller.php';

class Power_param extends REST_Controller
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
            $this->db->select('*','b.*');
            $this->db->from('das_power_param');
            $this->db->join('m_mesin as b','true');
            $this->db->where('id', $id);
            $data = $this->db->get()->result();
        } else {
           $qry ="Select a.*,b.kode_mesin,b.id_modbus from das_power_param a cross join  daspower_config b ";
           $data = $this->db->query($qry)->result();
            // $this->db->join('m_mesin as b','true');
            // $data = $this->db->get('das_power_param as a')->result(); 
        }

        $this->response($data, REST_Controller::HTTP_OK);
    }

    /**
     * Get All Data from this method.
     *
     * @return Response
     */
    public function index_post ()
    {
        if ($this->input->post()) {
            // Tangkap data POST
            $postData = $this->input->post("data");
            $json_data = json_decode($postData);
                //             UPDATE das_power_param 
                // SET param_unit = CASE	 param_id
                // 		WHEN 'VRN' THEN 'KV' 
                // 		WHEN 'VSN' THEN 'KV' 
                // 		ELSE ' ' 
                // 	END,
                // 	param_name = CASE param_id
                // 		WHEN 'VRN' THEN
                // 		'Voltage R' 
                // 		WHEN 'VSN' THEN
                // 		'Voltage N' ELSE ' ' 
                // 	END 
                // WHERE
                // 	param_id IN ( 'VRN', 'VSN' );
            $name="";
            $unit ="";
            $id = "";
            $divider="";
            foreach ($json_data  as $item) {  
            if (!isset($item->param_id)) {
                $item->param_id=" ";
            } 
            if (!isset($item->param_name)) {
                $item->param_name=" ";
            } 
              if (!isset($item->param_id)) {
                $item->param_id=" ";
            } 
            if (!isset($item->divider)) {
                $item->divider=1;
            }
                $name .= "WHEN '".$item->param_id."' THEN '".$item->param_name."' ";
                $unit .= "WHEN '".$item->param_id."' THEN '".$item->param_unit."' ";
                $divider .= "WHEN '".$item->param_id."' THEN '".$item->divider."' ";
                $id .= "'".$item->param_id."',";
            } 
            $qry = "UPDATE das_power_param 
                    SET param_unit = CASE param_id ".  $unit." END, param_name = CASE param_id ".$name." End,divider = CASE param_id ".$divider." End
                    
                    Where param_id IN (".substr($id, 0, -1).")";
            $res = $this->db->query($qry);
             if($res){
                $this->response(['Item updated successfully.'], REST_Controller::HTTP_OK);
             }
            //$this->response(['Item updated successfully.'], REST_Controller::HTTP_OK);
            //var_dump( $qry);

            // Simpan data ke dalam model atau lakukan proses lain yang diperlukan
           // $this->DataModel->saveData($postData);

            // Beri respons jika diperlukan
           // echo "Data telah disimpan.";
        } else {
            // Beri pesan jika tidak ada data POST yang diterima
            echo "Tidak ada data POST yang diterima.";
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
        $this->db->update('das_power_param', $input, array('id' => $id));

        $this->response(['Item updated successfully.'], REST_Controller::HTTP_OK);
    }

    /**
     * Get All Data from this method.
     *
     * @return Response
     */
    public function index_delete($id)
    {
        $this->db->delete('das_power_param', array('id' => $id));

        $this->response(['Item deleted successfully.'], REST_Controller::HTTP_OK);
    }
}
