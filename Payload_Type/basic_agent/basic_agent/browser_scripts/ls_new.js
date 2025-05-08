function(task, responses){
    if(responses.length > 0){
        return "<pre>" + responses[0].output + "</pre>";
    }
    return "<pre>No output received</pre>";
}