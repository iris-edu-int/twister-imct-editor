Ext.define("imct.utils.DateUtil", {
    singleton : true,
    utcDate : function() {var now = new Date();
        return new Date(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate(),  now.getUTCHours(), now.getUTCMinutes(), now.getUTCSeconds());
    }
});
