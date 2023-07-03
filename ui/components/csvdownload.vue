<template>
  <div>
    <v-container style="width: 100%; ">
   <v-btn>   
    <a color="indigo darken-4" style="color: rgb(99, 106, 165);" @click="downloadCSVTemplate">Download CSV Template</a>
  </v-btn> 
</v-container>
  </div>
</template>

<script>
export default {
  methods: {
    downloadCSVTemplate() {
      const csvContent ="name,email,mob,doj,aadhaar,pan,passport,sslc_regno,sslc_marks,sslc_passout,sslc_school,sslc_board,hse_regno,hse_marks,hse_passout,hse_school,hse_board,ug_regno,ug_specialization,ug_marks,ug_passout,ug_college,ug_university,pg_regno,pg_specialization,pg_marks,pg_passout,pg_college,pg_university,company_name,company_mail,empid,designation,lpa,start_date,end_date,hr_mail,reporting_manager"
      const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "template.csv";
      link.style.visibility = "hidden";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    },
  },
};
</script>