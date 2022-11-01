import { createApp } from 'vue'
import { createStore } from 'vuex'
import axios from "axios";


const storem = createStore({
    state: {
        materials: []
    },
    actions: {
        GET_MATERIALS({commit}) {
            return axios("http://localhost:8000/api/v1/materials", {
                method: 'GET'
                }
                ).then((response) => {
                    commit('SET_MATERIALS_TO_VUEX', response.data)
            })
        }
    },
    mutations: {
        SET_MATERIALS_TO_VUEX: (state, materials) => {
            state.materials = materials
        }
    },
    getters: {
        MATERIALS(state) {
            return state.materials;
        }
    }
})

export default storem;