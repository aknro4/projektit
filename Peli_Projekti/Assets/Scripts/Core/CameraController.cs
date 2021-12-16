using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class CameraController : MonoBehaviour
{
    public float turnSpeed;
    private Vector3 offset;
    public Transform player;

    private float minFov  = 15f;
    private float maxFov  = 90f;
    private float sensitivity  = 10f;
    

    private Camera cam;

    private void Start()
    {
        offset = new Vector3(7, 7,7);
    }

    private void Awake()
    {
        cam = Camera.main;
    }

    void LateUpdate()
    {
        Rotation();
        //Zoom();
    }

    private void Rotation()
    {
        offset = Quaternion.AngleAxis(Input.GetAxis("Horizontal") * turnSpeed, Vector3.up) * offset;
        offset = Quaternion.AngleAxis(Input.GetAxis("Vertical") * turnSpeed, Vector3.forward) * offset;
        transform.position = player.position + offset;
        transform.LookAt(player.position);   
    }

    private void Zoom()
    {
        float fov = Camera.main.fieldOfView;
        fov -= Input.GetAxis("Mouse ScrollWheel") * sensitivity;
        fov = Mathf.Clamp(fov, minFov, maxFov);
        Camera.main.fieldOfView = fov;
    }
}
