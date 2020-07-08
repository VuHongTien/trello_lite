import actions from "@/store/modules/tasks/actions";
import mutations from "@/store/modules/tasks/mutations";
import getters from "@/store/modules/tasks/getters";
import state from "@/store/modules/tasks/state";

export default {
    namespaced: true,
    actions, mutations, getters, state
}