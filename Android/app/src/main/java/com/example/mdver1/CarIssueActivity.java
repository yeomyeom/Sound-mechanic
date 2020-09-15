package com.example.mdver1;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import me.relex.circleindicator.CircleIndicator;

public class CarIssueActivity extends AppCompatActivity {
    ViewPager viewpager;
    CircleIndicator indicator;
    ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_carissue);
        setActionBar();

        viewpager = (ViewPager) findViewById(R.id.viewpager);
        indicator = (CircleIndicator) findViewById(R.id.indicator);
        listView = (ListView) findViewById(R.id.listView);

        final String[] listItem = getResources().getStringArray(R.array.carIssue_array);
        final ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                R.layout.list_item_carissue, R.id.list_item_text, listItem);

        listView.setAdapter(adapter);
        listView.setChoiceMode(ListView.CHOICE_MODE_SINGLE);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int position, long l) {
                String value = adapter.getItem(position);
                viewpager.setCurrentItem(position);
            }
        });
        viewpager.setAdapter(new CarIssuePagerAdapter());
        indicator.setViewPager(viewpager);

        viewpager.addOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {

            }

            @Override
            public void onPageSelected(int position) {
                listView.setItemChecked(position, true);
            }

            @Override
            public void onPageScrollStateChanged(int state) {
            }
        });
    }

    private void setActionBar() {
        CustomActionBar ca = new CustomActionBar(this, getSupportActionBar());
        ca.setActionBar();
    }

}
