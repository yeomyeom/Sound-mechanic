package com.example.mdver1;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.widget.Toolbar;
import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;


public class CustomActionBar {
    private Activity activity;
    private ActionBar actionBar;

    public CustomActionBar(Activity _activity, ActionBar _actionBar){
        this.activity = _activity;
        this.actionBar=_actionBar;
    }


    public void setActionBar(){
        actionBar.setDisplayShowCustomEnabled(true);
        actionBar.setDisplayHomeAsUpEnabled(false);
        actionBar.setDisplayShowTitleEnabled(false);
        actionBar.setDisplayShowHomeEnabled(false);

        View mCustomView=LayoutInflater.from(activity).inflate(R.layout.actionbar_actions,null);
        actionBar.setCustomView(mCustomView);
    }
}
