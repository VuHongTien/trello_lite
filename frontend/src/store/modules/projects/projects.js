import actions from "@/store/modules/projects/actions";
import mutations from "@/store/modules/projects/mutations";
import getters from "@/store/modules/projects/getters";
import state from "@/store/modules/projects/state";

export default {
    namespaced: true,
    actions, mutations, getters, state
}