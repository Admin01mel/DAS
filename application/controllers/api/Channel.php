<?php
   
require APPPATH . 'libraries/REST_Controller.php';
     
class Channel extends REST_Controller {
    
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
	// public function index_get($id = 0)
	// {
    //     $this->db->select('*');
    //     $this->db->from('user_notif');
    //     $data = $this->db->get()->result();
     
    //     $this->response($data, REST_Controller::HTTP_OK);
	// }
      
    /**
     * Get All Data from this method.
     *
     * @return Response
    */
   
    public function index_post()
    {
        $input = $this->input->post();
     //   echo $input[0]->name;
        $data =json_decode($input["data"]);
        $nama_alat="";
        $high="";
        $low="";
        $chn ="";
        $channel="";
        $machine_code="";
        for($i =0 ; $i<count($data);$i++){
            $no = "CHN".$i;
            $chn =  intval(str_replace(['CHN'], '',$data[$i]->port ));
            $nama_alat .="WHEN ".$chn." THEN '".$data[$i]->name."' ";
            $high .= "WHEN  ".$chn." THEN '".$data[$i]->high."' ";
            $low .= "WHEN  ".$chn." THEN '".$data[$i]->low."' ";
            $machine_code= $data[$i]->machine_code;
            $channel .="$chn,";
        }
        $channel = substr($channel, 0, -1);
        $check = "SELECT * from m_mesin where kode_mesin = '$machine_code'";
        
        $qry= "UPDATE mesin
                    SET 
                        nama_alat = CASE port
                                    $nama_alat
                                    ELSE nama_alat
                                    END,
                        high = CASE port
                                    $high
                                ELSE high
                            END,
                        low = CASE port
                            $low
                                ELSE low
                            END
                    WHERE port IN ( $channel) and kode_mesin = '".$machine_code."';";
          $res_check = $this->db->query($check);
         
          if(count($res_check->result())>0){
            $res = $this->db->query($qry);
              $res_check = $this->db->query($check);
              if($res==1){
                $this->response(['Item updated successfully.'], REST_Controller::HTTP_OK);
              }
          }
          else{

            $this->response(['Invalid Serial Number'], REST_Controller::HTTP_METHOD_NOT_ALLOWED );
             
          }
       
          

    }  
     
    /**
     * Get All Data from this method.
     *
     * @return Response
    */
    // public function index_put($id)
    // {
    //     $input = $this->put();
    //     $this->db->update('items', $input, array('id'=>$id));
     
    //     $this->response(['Item updated successfully.'], REST_Controller::HTTP_OK);
    // }
     
    /**
     * Get All Data from this method.
     *
     * @return Response
    */
    // public function index_delete($id)
    // {
    //     $this->db->delete('items', array('id'=>$id));
       
    //     $this->response(['Item deleted successfully.'], REST_Controller::HTTP_OK);
    // }
    	
}