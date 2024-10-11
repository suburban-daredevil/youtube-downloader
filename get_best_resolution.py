def select_best_res(yt):
    stream_list = yt.streams.filter(type="video", mime_type="video/mp4").order_by("resolution")

    res_ceiling = 1080 # maximum resolution

    # selector for last stream (and therefore should be highest resolution) in ordered resolution list
    downward_moving_resolution_selector = -1
    while int(
            stream_list[downward_moving_resolution_selector].resolution.rstrip("p")
    ) > int(res_ceiling):
        downward_moving_resolution_selector -= 1
    best_res_stream = stream_list[downward_moving_resolution_selector]

    return best_res_stream