using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RPG.Core
{
    public class FollowCamera : MonoBehaviour
    {
        //public float turnSpeed;
        //private Vector3 offset;

        [SerializeField] Transform target;

        //private void Start()
        //{
        //    offset = new Vector3(target.position.x, target.position.y, target.position.z);
        //}

        void LateUpdate()
        {
            //Roation();
            transform.position = target.position;
            //transform.position = target.position + offset;
        }

        //private void Roation()
        //{
        //    offset = Quaternion.AngleAxis(Input.GetAxis("Horizontal") * turnSpeed, Vector3.up) * offset;
        //    offset = Quaternion.AngleAxis(Input.GetAxis("Vertical") * turnSpeed, Vector3.forward) * offset;
        //    transform.position = target.position + offset;
        //    transform.LookAt(target.position);
        //}
    }
}
