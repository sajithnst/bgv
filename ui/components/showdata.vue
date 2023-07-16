<template>
      <v-container fluid class="d-flex align-center justify-center">
        <v-card class="text-center" :elevation="6" :height="auto" :width="700">
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
                          
                      <v-row>
                        <v-col>
                          <v-container class="text-center">
                            <v-btn size="20%"  :loading="isLoading" :disabled="isLoading" color="indigo darken-4" style="color:white" @click="inserted()">Inserted Data</v-btn>
                          </v-container>
                        </v-col>
                        <v-col>
                          <v-container class="text-center">
                            <v-btn size="20%"  :loading="isLoading" :disabled="isLoading" color="indigo darken-4" style="color:white" @click="deleted()">Deleted Data</v-btn>
                          </v-container>
                        </v-col>
                      </v-row>
                    </v-card>
          </v-container>
  </template>
  <script>
  export default {
    name: 'hseupload',
    data: () => ({
        data:{},
        isLoading: false
  
      }),
    methods:{

   
    
    }
    
  };
  </script>
  