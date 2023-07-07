<template>
  <v-container>
      <v-container class="text-center" >
          <v-row>
            <v-card class="text-center" :elevation="6" :height="auto" :width="700">
              <br>
              <v-text-title><h2>Personal Data</h2></v-text-title>
              <br>
              <v-row>
                  <v-col>
                      <v-container >
                        <v-container style="width: 100%; ">
                          <v-btn>   
                           <a color="indigo darken-4" style="color: rgb(99, 106, 165);" @click="downloadCSVTemplate">Download Personal Template</a>
                         </v-btn> 
                       </v-container>
                      </v-container>
                  </v-col>
                  <v-col>
                      <v-container class="text-center">
                          <v-file-input @change="fileselect" style="width:70%; margin:0 auto; " label="File input" variant="solo-filled"></v-file-input>
                          <v-btn color="indigo darken-4" style="color:white" @click="upload()">Upload</v-btn><br/><br/>
                        </v-container>
                  </v-col>
              </v-row>
              <v-row>     
                <v-container class="text-center">
                  <h3 v-if="this.data.total_count">Uploaded Details:</h3>
                </v-container>               
              </v-row>
              <v-row>
                <v-col>
                  <v-container>
                    <v-card-subtitle v-if="this.data.total_count">Total count: {{ this.data.total_count }}</v-card-subtitle>
                  </v-container>

                </v-col>
                <v-col>
                  <v-container>
                    <v-card-subtitle v-if="this.data.insert_count">Insert count: {{ this.data.insert_count }}</v-card-subtitle>
                  </v-container>
                </v-col>
                <v-col>
                  <v-container>
                    <v-card-subtitle v-if="this.data.delete_count">Delete count: {{ this.data.delete_count }}</v-card-subtitle>
                  </v-container>
                </v-col>
                
              </v-row>

            </v-card>
          </v-row>
    
    
        </v-container>
  </v-container>
</template>
<script>
export default {
  name: 'pgupload',
  methods:{
    async fileselect(event){
        this.file=event
      },
    async upload(){
        let formdata= new FormData()
            formdata.append('csv_file',this.file)
            let furl = "http://127.0.0.1:8000/hr/uploadpg"
            let res = await this.$axios.post(furl, formdata);
            console.log(res.data)
    }
  },

    downloadCSVTemplate() {
      const csvContent ="name,email,pg_regno,pg_specialization,pg_marks,pg_passout,pg_college,pg_university"
      const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "pg.csv";
      link.style.visibility = "hidden";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    },
 
}
</script>