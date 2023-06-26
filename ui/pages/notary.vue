<template>
  <v-container>
    <br>
      <v-container>
        <v-row>
          <v-col>
            <v-card height="180.5px">
              <v-card-title>Total Profiles</v-card-title>
              <v-card-title><h1 style="font-weight: normal; font-size: 70px;" >{{ counts }}</h1></v-card-title>
            </v-card>
          </v-col>
          <v-col>
            <v-card>

              <v-card-title>PENDING PROFILES</v-card-title>
              <v-card-title><h1 style="font-weight: normal; font-size: 70px;" >{{ count }}</h1></v-card-title>
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
                      color="red"
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
              <v-card-title><h1 style="font-weight: normal; font-size: 70px;" >{{ count1 }}</h1></v-card-title>
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
              color="red"
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
    let url = "http://127.0.0.1:8000/pendinguser"
        let res = await this.$axios.get(url)
        this.profiles = res.data.list
        this.count = res.data.count

    let surl = "http://127.0.0.1:8000/verifiedusers"
    let sres = await this.$axios.get(surl)
    this.count1 = sres.data.count1

    let turl = "http://127.0.0.1:8000/totalprofile"
    let tres = await this.$axios.get(turl)
    this.counts = tres.data.counts

  },
  data: () => ({
      reveal: false,
      approve: false,
      count:{},
      count1:{},
      counts:{}
    }),

}
</script>

