<template>
  <v-container>
    <br>
      <v-container class="text-center">
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>PENDING PROFILES</v-card-title>
              <v-card-actions>
                <v-btn
                  text
                  color="indigo darken-4"
                  @click="reveal = true"
                >
                  Show
                </v-btn>
              </v-card-actions>
              <v-expand-transition>
                <v-card
                  v-if="reveal"
                  class="transition-fast-in-fast-out v-card--reveal"
                  style="height: 100%;"
                >
                  <notaryusers/>
                  <v-card-actions class="pt-0">
                    <v-btn
                      text
                      color="indigo darken-4"
                      @click="reveal = false"
                    >
                      Close
                    </v-btn>
                  </v-card-actions>
                </v-card>

              </v-expand-transition>
            </v-card>

          </v-col>
          <v-col>
            <v-card>
              <v-card-title>COMPLETED PROFILE</v-card-title>
            <v-card-actions>
              <v-btn
                text
                color="indigo darken-4"
                @click="approve = true"
              >
                Show
              </v-btn>
            </v-card-actions>
            <v-expand-transition>
              <v-card
          v-if="approve"
          class="transition-fast-in-fast-out v-card--reveal"
          style="height: 100%;"
        >

            <notaryapproved/>


          <v-card-actions class="pt-0">
            <v-btn
              text
              color="indigo darken-4"
              @click="approve = false"
            >
              Close
            </v-btn>
          </v-card-actions>
        </v-card>
            </v-expand-transition>
          </v-card>
          </v-col>

        </v-row>

      </v-container>



  </v-container>
</template>
<script>
export default {
  name :"notary",
  layout: "notary_layout",
  async mounted(){
    this.$vuetify.theme.dark =false;
  },
  data: () => ({
      reveal: false,
      approve: false,
    }),

}
</script>


