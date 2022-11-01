// import { createApp } from 'vue'
import { createStore  } from 'vuex'
import { getAPI } from './api'
import axios from "axios";

// const Vue = createApp()

// Vue.use(Vuex)

export default createStore ({
  state: {
    materials: [],
     accessToken: null,
     refreshToken: null,
     APIData: ''
  },
  mutations: {
     SET_MATERIALS_TO_VUEX: (state, materials) => {
            state.materials = materials
        },
    updateStorage (state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
    }
  },
  getters: {
    loggedIn (state) {
      return state.accessToken != null
    },
    MATERIALS(state) {
            return state.materials;
        }
  },
  actions: {
      GET_MATERIALS({commit}) {
          return axios("http://localhost:8000/api/v1/materials", {
                  method: 'GET'
              }
          ).then((response) => {
              commit('SET_MATERIALS_TO_VUEX', response.data)
          })
      },
      userLogout(context) {
          if (context.getters.loggedIn) {
              context.commit('destroyToken')
              localStorage.removeItem('token')
          }
      },
      userLogin(context, usercredentials) {
          return new Promise((resolve, reject) => {
              getAPI.post('api/v1/login', {
                  username: usercredentials.username,
                  password: usercredentials.password
              })
                  .then(response => {
                      console.log(response)
                      context.commit('updateStorage', {
                          access: response.data.access_token,
                          refresh: response.data.refresh_token
                      })
                      resolve()
                  })
                  .catch(err => {
                      reject(err)
                  })
          })
      },
      addMaterial(context, materialCredentials) {
             // let token = localStorage.getItem('token')
          return new Promise((resolve, reject) => {

              getAPI.post('api/v1/materials', {
                  name: materialCredentials.name,
                  iron_amount: materialCredentials.iron_amount,
                  silicon_amount: materialCredentials.silicon_amount,
                  aluminum_amount: materialCredentials.aluminum_amount,
                  sodium_amount: materialCredentials.sodium_amount,
                  sulfur_amount: materialCredentials.sulfur_amount,
                  month: materialCredentials.month,
                  headers: { Authorization: `Bearer ${this.$store.state.accessToken}` }

              }).then(response => {
                  console.log(response)
                  context.commit('updateStorage', {
                      access: response.data.access_token,
                      refresh: response.data.refresh_token
                  })
                  resolve()
              })
                  .catch(err => {
                      reject(err)
                  })
          })
      },
  }})

