package com.example.mdver1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class purpose extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_purpose);

        setActionBar();
    }

    private void setActionBar(){
        CustomActionBar ca=new CustomActionBar(this, getSupportActionBar());
        ca.setActionBar();
    }
}
