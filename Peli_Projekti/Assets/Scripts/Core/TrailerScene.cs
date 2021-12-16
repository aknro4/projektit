﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Video;
using UnityEngine.SceneManagement;

public class TrailerScene : MonoBehaviour
{
    VideoPlayer video;

    // Start is called before the first frame update
    void Start()
    {
        video = GetComponent<VideoPlayer>();
        video.Play();
        video.loopPointReached += OnMovieEnded;
    }

    void OnMovieEnded(UnityEngine.Video.VideoPlayer vp)
    {
        SceneManager.LoadScene("Sandbox");
    }
}