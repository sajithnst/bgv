<template>
  <v-container>
    <br>
      <v-container>

        <v-row>
          <v-col>
            <v-card width="99%">
              <v-container class="text-center">
                <h4>&ensp; Current Login: &ensp; &ensp;{{ pdata.login_date }}</h4>

              </v-container>
            </v-card>
          </v-col>
          <v-col>
            <v-card width="97%">
              <v-container class="text-center">
                <h4 v-if="pdata.last_login">&ensp; Last Login: &ensp;&ensp;{{ pdata.last_login }}</h4>

              </v-container>

            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <v-card height="180.5px">
              <v-card-title>Total </v-card-title>
              <v-card-title><h1 style="font-weight: normal; font-size: 70px;" >{{ counts }}</h1></v-card-title>
            </v-card>
          </v-col>
          <v-col>
            <v-card>

              <v-card-title>PENDING </v-card-title>
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

              <v-card-title>INPROGRESS </v-card-title>
              <v-card-title><h1 style="font-weight: normal; font-size: 70px;" >{{ count2 }}</h1></v-card-title>
              <v-card-actions>
                <v-btn
                  text
                  color="indigo darken-4"
                  @click="reveal2 = true"
                >
                  Show
                </v-btn>
              </v-card-actions>
              <v-expand-transition>
                <v-card
                  v-if="reveal2"
                  class="transition-fast-in-fast-out v-card--reveal"
                  style="height: 100%;"
                >
                  <notaryinprogress/>

                  <v-card-actions class="pt-0">
                    <v-btn
                      text
                      color="red"
                      @click="reveal2 = false"
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
              <v-card-title>COMPLETED </v-card-title>
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

        let rurl = "http://127.0.0.1:8000/inprogressuser"
    let rres = await this.$axios.get(rurl)
    this.count2 = rres.data.count


    let surl = "http://127.0.0.1:8000/verifiedusers"
    let sres = await this.$axios.get(surl)
    this.count1 = sres.data.count1

    let turl = "http://127.0.0.1:8000/totalprofile"
    let tres = await this.$axios.get(turl)
    this.counts = tres.data.counts

   

    this.$vuetify.theme.dark =false;
    this.email = this.$storage.getUniversal('notaryemail')
    let nurl = "http://127.0.0.1:8000/notary"
    let nres = await this.$axios.get(nurl,{params:{ email :this.email}});
    this.pdata = nres.data
    console.log(this.pdata)

  },
  data: () => ({
      reveal: false,
      reveal2:false,
      approve: false,
      count:{},
      count1:{},
      count2:{},
      counts:{},
      pdata:{}
    }),

}
</script>

