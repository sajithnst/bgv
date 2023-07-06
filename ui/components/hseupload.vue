<template>
    <v-container>
        <v-container class="text-center" >
            <v-row>
              <v-sheet class="text-center" :elevation="6" :height="300" :width="700">
                <br>
                <v-text-title><h2>HSE Data</h2></v-text-title>
                <br>
                <v-row>
                    <v-col>
                        <v-container style="margin-top:10%">
                            <v-container style="width: 100%; ">
                                <v-btn>   
                                 <a color="indigo darken-4" style="color: rgb(99, 106, 165);" @click="downloadCSVTemplate">Download HSE Template</a>
                               </v-btn> 
                             </v-container>
                        </v-container>
                    </v-col>
                    <v-col>
                        <v-container>
                            <v-file-input @change="fileselect" style="width:70%; margin:0 auto; margin-top:4%;" label="File input" variant="solo-filled"></v-file-input>
                            <v-btn color="indigo darken-4" style="color:white" @click="upload()">Upload</v-btn><br/><br/>
                          </v-container>
                    </v-col>
                </v-row>
              </v-sheet>
            </v-row>
      
      
          </v-container>
    </v-container>
</template>
<script>
export default {
  name: 'hseupload',
  methods:{
    async fileselect(event){
        this.file=event
      },
    async upload(){
        let formdata= new FormData()
            formdata.append('csv_file',this.file)
            let furl = "http://127.0.0.1:8000/hr/uploadhse"
            let res = await this.$axios.post(furl, formdata);
            console.log(res.data)
    },
    methods: {
    downloadCSVTemplate() {
      const csvContent ="name,email,hse_regno,hse_marks,hse_passout,hse_school,hse_board"
      const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "hse.csv";
      link.style.visibility = "hidden";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    },
   }
  }
};
</script>
